#!/usr/bin/env python3
"""Portable structural validation for a Talia production node_graph.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def validate(path: Path) -> tuple[list[str], list[str], dict]:
    graph = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    raw_nodes = graph.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        return ["nodes must be a non-empty array"], warnings, graph

    ids = [node.get("id") for node in raw_nodes]
    if any(not isinstance(node_id, str) or not node_id for node_id in ids):
        errors.append("every node needs a non-empty string id")
    if len(set(ids)) != len(ids):
        errors.append("node ids must be unique")
    nodes = {node.get("id"): node for node in raw_nodes if node.get("id")}
    start = graph.get("start")
    if start not in nodes:
        errors.append(f"start node {start!r} does not exist")

    ending_ids = {node_id for node_id, node in nodes.items() if node.get("type") == "ending"}
    if not ending_ids:
        errors.append("at least one ending node is required")

    image_ids: set[str] = set()
    for node_id, node in nodes.items():
        beats = node.get("beats") or []
        if not beats:
            warnings.append(f"{node_id}: no beats")
        for beat in beats:
            image_id = beat.get("img")
            if not image_id:
                errors.append(f"{node_id}: beat missing img id")
            elif image_id in image_ids:
                errors.append(f"duplicate img id {image_id!r}")
            else:
                image_ids.add(image_id)
            if not beat.get("prompt") and not beat.get("card"):
                warnings.append(f"{node_id}/{image_id}: no prompt or card")

        choices = node.get("choices") or []
        if node.get("type") == "ending" and choices:
            warnings.append(f"{node_id}: ending has choices")
        if node.get("type") != "ending" and not choices:
            errors.append(f"{node_id}: non-ending dead end")
        normal_choices = []
        for choice in choices:
            target = choice.get("target")
            if target not in nodes:
                errors.append(f"{node_id}: choice targets missing node {target!r}")
            if choice.get("type", "normal") == "normal":
                normal_choices.append(choice)
            region = choice.get("tap_region") or choice.get("region")
            if region is not None:
                if isinstance(region, dict):
                    region = [region.get(key) for key in ("x", "y", "w", "h")]
                if not isinstance(region, (list, tuple)) or len(region) != 4:
                    errors.append(f"{node_id}: tap region must be [x,y,w,h]")
                elif any(not isinstance(v, (int, float)) for v in region):
                    errors.append(f"{node_id}: tap region values must be numbers")
                elif any(v < 0 or v > 1 for v in region) or region[0] + region[2] > 1 or region[1] + region[3] > 1:
                    errors.append(f"{node_id}: tap region is outside normalized bounds")
        if node.get("auto_advance") and len(normal_choices) != 1:
            errors.append(f"{node_id}: auto_advance requires exactly one normal choice")

    reachable: set[str] = set()
    stack = [start] if start in nodes else []
    while stack:
        node_id = stack.pop()
        if node_id in reachable:
            continue
        reachable.add(node_id)
        stack.extend(
            choice.get("target")
            for choice in nodes[node_id].get("choices", [])
            if choice.get("target") in nodes
        )
    for node_id in nodes:
        if node_id not in reachable:
            errors.append(f"{node_id}: unreachable from start")
    for ending_id in ending_ids:
        if ending_id not in reachable:
            errors.append(f"{ending_id}: ending is unreachable")
    return errors, warnings, graph


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_node_graph.py path/to/node_graph.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1]).resolve()
    try:
        errors, warnings, graph = validate(path)
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)], "warnings": []}, indent=2))
        return 2
    result = {
        "ok": not errors,
        "project": (graph.get("project") or {}).get("id"),
        "nodes": len(graph.get("nodes") or []),
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
