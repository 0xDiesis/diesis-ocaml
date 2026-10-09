# Diesis OCaml SDK

OCaml bindings with Zarith integers and a C bridge to abi-typegen-runtime.

Includes bindings for 29 public system contracts and `canonical.json` with chain
configuration and addresses. Generated with exact **abi-typegen 0.8.0**.

## Regenerate

Install [abi-typegen 0.8.0](https://github.com/doublesharp/abi-typegen/releases/tag/v0.8.0)
and compile the Diesis contracts. From this repository:

```sh
DIESIS_CONTRACTS_DIR=/path/to/diesis-contracts python3 scripts/generate.py
DIESIS_CONTRACTS_DIR=/path/to/diesis-contracts python3 scripts/generate.py --check
```

The full Diesis workspace uses `../../diesis-core/diesis/contracts` by default.
Set `ABI_TYPEGEN` to select a binary explicitly. Other versions are rejected.
`generation.json` records the contract selection and exact generator version.
`canonical.json` is vendored from `diesis-js`; refresh it when chain configuration changes.

## Use

Compilation requires OCaml, ocamlfind, and Zarith. Compile each generated `.ml`
with `ocamlfind ocamlc -package zarith -c`, then compile its `.ocaml.c` bridge.
Link the selected modules and bridges with `-custom -package zarith -linkpkg`
and `libabi_typegen_runtime` from the abi-typegen-runtime 0.8.0 build. Addresses and
bytes are raw strings. Integers use `Z.t`.


## Validation

All generated modules passed local compilation or loading. Codec checks cover
large integers and representative Diesis ABI values; all 221 event definitions
passed independent fixtures in q. These checks do not establish live Diesis RPC
qualification. See the parent workspace's SDK validation reports for full evidence.
