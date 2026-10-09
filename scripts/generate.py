#!/usr/bin/env python3
"""Regenerate contract bindings with the pinned abi-typegen release."""
import argparse
import json
import os
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
config = json.loads((root / "generation.json").read_text())
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
binary = os.environ.get("ABI_TYPEGEN", "abi-typegen")
try:
    version = subprocess.run([binary, "--version"], check=True, capture_output=True, text=True).stdout.strip()
except (OSError, subprocess.CalledProcessError) as error:
    parser.error(f"install abi-typegen {config['version']} or set ABI_TYPEGEN: {error}")
if version != f"abi-typegen {config['version']}":
    parser.error(f"abi-typegen {config['version']} is required; found {version!r}")
contracts = Path(os.environ.get("DIESIS_CONTRACTS_DIR", root / "../../diesis-core/diesis/contracts")).resolve()
command = [binary, "generate", "--artifacts", str(contracts / "out"),
           "--contracts", ",".join(config["contracts"]), "--target", config["target"],
           "--out", str(root / "generated")]
if args.check:
    command.append("--check")
subprocess.run(command, check=True)
