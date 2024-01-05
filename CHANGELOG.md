# Changelog

<!-- changelogging: start -->

## 2.0.0 (2024-01-05)

### Features

- Allow defining entry points implicitly (without providing the `__name__`).
  The name will instead be fetched from the `__module__` of the function provided.

### Changes

- `entrypoint` now uses `named` and `typing-aliases` under the hood.

## 1.4.0 (2023-04-16)

### Changes

- `entrypoint` now uses `attrs` under the hood.

### Features

- `Main` type alias is now exported from `entrypoint`:

  ```python
  Main = Callable[[], None]
  ```

  Note that this ensures `main` functions do not return anything at type-checking time.

## 1.3.0 (2022-07-06)

No significant changes.

## 1.2.6 (2022-07-06)

No significant changes.

## 1.2.5 (2022-07-03)

No significant changes.

## 1.2.4 (2022-06-29)

No significant changes.

## 1.2.3 (2022-06-28)

No significant changes.

## 1.2.2 (2022-06-28)

No significant changes.

## 1.2.1 (2022-06-25)

No significant changes.

## 1.2.0 (2022-06-25)

### Changes

- `entrypoint.py -> entrypoint` migration. ([#20](https://github.com/nekitdev/entrypoint/pull/20))

## 1.1.2 (2022-06-24)

No significant changes.

## 1.1.1 (2022-06-24)

No significant changes.

## 1.1.0 (2022-06-24)

### Features

- Add documentation.

## 1.0.1 (2022-06-21)

No significant changes.

## 1.0.0 (2022-06-06)

Initial stable release.

## 0.3.1 (2022-05-25)

No significant changes.

## 0.3.0 (2022-04-18)

### Changes

- Exported the following constant:

  ```python
  MAIN = "__main__"
  ```

  `MAIN` can be used to ensure *entry points* will always get called.
  ([#11](https://github.com/nekitdev/entrypoint/pull/11))

## 0.2.0 (2022-04-17)

### Internal

- Migrated from module to library layout. ([#9](https://github.com/nekitdev/entrypoint/pull/9))

## 0.1.3 (2022-04-17)

No significant changes.

## 0.1.2 (2022-04-17)

No significant changes.

## 0.1.1 (2022-04-11)

No significant changes.

## 0.1.0 (2022-04-11)

Initial release.
