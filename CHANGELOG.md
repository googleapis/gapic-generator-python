# Changelog

### [0.32.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.1...v0.32.2) (2020-08-20)


### Bug Fixes

* add 'type: ignore' comment for 'google.auth' ([#579](https://www.github.com/googleapis/gapic-generator-python/issues/579)) ([af17501](https://www.github.com/googleapis/gapic-generator-python/commit/af17501d258c7c37fc1081fcad5fe18f7629f4c3))

### [0.32.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.0...v0.32.1) (2020-08-19)


### Bug Fixes

* rename local var page in generated tests ([#577](https://www.github.com/googleapis/gapic-generator-python/issues/577)) ([075f9e8](https://www.github.com/googleapis/gapic-generator-python/commit/075f9e8d50b02ffb5f2f042b84f27a9f634636e2))

## [0.32.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.31.1...v0.32.0) (2020-08-17)


### Features

* allow user-provided client info ([#573](https://www.github.com/googleapis/gapic-generator-python/issues/573)) ([b2e5274](https://www.github.com/googleapis/gapic-generator-python/commit/b2e52746c7ce4b983482fb776224b30767978c79)), closes [googleapis/python-kms#37](https://www.github.com/googleapis/python-kms/issues/37) [#566](https://www.github.com/googleapis/gapic-generator-python/issues/566)

### [0.31.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.31.0...v0.31.1) (2020-08-17)


### Bug Fixes

* install gcc by hand ([#571](https://www.github.com/googleapis/gapic-generator-python/issues/571)) ([e224a03](https://www.github.com/googleapis/gapic-generator-python/commit/e224a0365a2d3ed20d69cf4d1298a3f022f8da76))

## [0.31.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.30.0...v0.31.0) (2020-07-28)


### Features

* bypass request copying in method calls ([#557](https://www.github.com/googleapis/gapic-generator-python/issues/557)) ([3a23143](https://www.github.com/googleapis/gapic-generator-python/commit/3a2314318de229a3353c984a8cb2766ae95cc968))


### Bug Fixes

* add google.api_core.retry import to base.py ([#555](https://www.github.com/googleapis/gapic-generator-python/issues/555)) ([1d08e60](https://www.github.com/googleapis/gapic-generator-python/commit/1d08e60cea4c5b3fa2555a4952161b0115d686f2))

## [0.30.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.29.2...v0.30.0) (2020-07-27)


### Features

* precache wrapped rpcs ([#553](https://www.github.com/googleapis/gapic-generator-python/issues/553)) ([2f2fb5d](https://www.github.com/googleapis/gapic-generator-python/commit/2f2fb5d3d9472a79c80be6d052129d07d2bbb835))

### [0.29.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.29.1...v0.29.2) (2020-07-23)


### Bug Fixes

* rename __init__.py to __init__.py.j2 ([#550](https://www.github.com/googleapis/gapic-generator-python/issues/550)) ([71a7062](https://www.github.com/googleapis/gapic-generator-python/commit/71a7062b918136b916cc5bfc7dbdf64f870edf6a)), closes [#437](https://www.github.com/googleapis/gapic-generator-python/issues/437)

### [0.29.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.29.0...v0.29.1) (2020-07-23)


### Bug Fixes

* use context manager for mtls env var ([#548](https://www.github.com/googleapis/gapic-generator-python/issues/548)) ([d19e180](https://www.github.com/googleapis/gapic-generator-python/commit/d19e1808df9cd2884ae7a449977a479b4829bc1d))

## [0.29.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.28.1...v0.29.0) (2020-07-22)


### Features

* add iam methods to templates ([#545](https://www.github.com/googleapis/gapic-generator-python/issues/545)) ([3f42c3c](https://www.github.com/googleapis/gapic-generator-python/commit/3f42c3cf8aae432a9bda0953fbabd7f0c8d774de))
* support quota project override via client options ([#496](https://www.github.com/googleapis/gapic-generator-python/issues/496)) ([bbc6b36](https://www.github.com/googleapis/gapic-generator-python/commit/bbc6b367f50526312e8320f0fc668ef88f230dbd))


### Bug Fixes

* make # after alpha/beta optional ([#540](https://www.github.com/googleapis/gapic-generator-python/issues/540)) ([f86a47b](https://www.github.com/googleapis/gapic-generator-python/commit/f86a47b6431e374ae1797061511b49fe6bf22daf))

### [0.28.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.28.0...v0.28.1) (2020-07-16)


### Bug Fixes

* remove typo from py_gapic.bzl ([#532](https://www.github.com/googleapis/gapic-generator-python/issues/532)) ([2975c2d](https://www.github.com/googleapis/gapic-generator-python/commit/2975c2d76e08b5ee5324730707707d9dd6ced8ae))

## [0.28.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.27.0...v0.28.0) (2020-07-16)


### Features

* add retry config passed to bazel rule ([#526](https://www.github.com/googleapis/gapic-generator-python/issues/526)) ([9e96151](https://www.github.com/googleapis/gapic-generator-python/commit/9e96151d702786912fcf033f7535efad8ae754ee))


### Bug Fixes

* paged code and templates are no longer message centric ([#527](https://www.github.com/googleapis/gapic-generator-python/issues/527)) ([00ba77c](https://www.github.com/googleapis/gapic-generator-python/commit/00ba77c3d27ef9a0b8742db3660983b80a68c672))

## [0.27.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.6...v0.27.0) (2020-07-13)


### Features

* support for proto3 optional fields ([#519](https://www.github.com/googleapis/gapic-generator-python/issues/519)) ([1aa729c](https://www.github.com/googleapis/gapic-generator-python/commit/1aa729cc8d2f7f0de25c8348fdbf9d6dd96f5847))

### [0.26.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.5...v0.26.6) (2020-07-10)


### Bug Fixes

* primitive repeated fields are now correctly auto paginated ([#517](https://www.github.com/googleapis/gapic-generator-python/issues/517)) ([61a2cc0](https://www.github.com/googleapis/gapic-generator-python/commit/61a2cc0d4c08064d442fd4d7aa4b1b9e56158eaa))

### [0.26.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.4...v0.26.5) (2020-07-10)


### Bug Fixes

* convert datetime back to proto for unit tests ([#511](https://www.github.com/googleapis/gapic-generator-python/issues/511)) ([e1c787d](https://www.github.com/googleapis/gapic-generator-python/commit/e1c787d3b6fe09dc0b4e00f07a7bd77fb5f1e6a3))

### [0.26.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.3...v0.26.4) (2020-07-10)


### Bug Fixes

* require min google-api-core version of 1.21.0 ([#506](https://www.github.com/googleapis/gapic-generator-python/issues/506)) ([bf787bd](https://www.github.com/googleapis/gapic-generator-python/commit/bf787bd36198288d6a40e45e44e43f0098cfec7c)), closes [#461](https://www.github.com/googleapis/gapic-generator-python/issues/461)
* tweak oneof detection ([#505](https://www.github.com/googleapis/gapic-generator-python/issues/505)) ([1632e25](https://www.github.com/googleapis/gapic-generator-python/commit/1632e250cfc01a17ccad128c3e065008b334473a))

### [0.26.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.2...v0.26.3) (2020-07-08)


### Bug Fixes

* fix wrong unit test ([#502](https://www.github.com/googleapis/gapic-generator-python/issues/502)) ([c95bd45](https://www.github.com/googleapis/gapic-generator-python/commit/c95bd45506df7973758b9e1249586597d8214985))

### [0.26.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.1...v0.26.2) (2020-07-07)


### Bug Fixes

* add oneof fields to generated protoplus init ([#485](https://www.github.com/googleapis/gapic-generator-python/issues/485)) ([be5a847](https://www.github.com/googleapis/gapic-generator-python/commit/be5a847aeff6687679f7bca46308362d588f5c77)), closes [#484](https://www.github.com/googleapis/gapic-generator-python/issues/484)

### [0.26.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.26.0...v0.26.1) (2020-07-07)


### Bug Fixes

* pass metadata to pagers ([#470](https://www.github.com/googleapis/gapic-generator-python/issues/470)) ([c43c6d9](https://www.github.com/googleapis/gapic-generator-python/commit/c43c6d943fa99f202014bf4bba795df25d314a63)), closes [#469](https://www.github.com/googleapis/gapic-generator-python/issues/469)

## [0.26.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.25.2...v0.26.0) (2020-06-30)


### Features

* add `credentials_file` and `scopes` via `client_options` ([#461](https://www.github.com/googleapis/gapic-generator-python/issues/461)) ([b5e1b1e](https://www.github.com/googleapis/gapic-generator-python/commit/b5e1b1e8991159dc176da889e9bdf12e3eebdb1e))


### Bug Fixes

* add name and version info to fixup script name ([#490](https://www.github.com/googleapis/gapic-generator-python/issues/490)) ([16fe7e7](https://www.github.com/googleapis/gapic-generator-python/commit/16fe7e7885b7e17bf16b4f1f8f8844b9f5d0bdfe))
* Temporarily define a fixed testing event loop ([#493](https://www.github.com/googleapis/gapic-generator-python/issues/493)) ([2d22d91](https://www.github.com/googleapis/gapic-generator-python/commit/2d22d919bc8c08e03f501ff2f23152b761467c80))

### [0.25.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.25.1...v0.25.2) (2020-06-23)


### Bug Fixes

* always use dataclasses 0.6 ([#481](https://www.github.com/googleapis/gapic-generator-python/issues/481)) ([066d04e](https://www.github.com/googleapis/gapic-generator-python/commit/066d04e7d53301024106f244280502f16af46b79))

### [0.25.1](https://www.github.com/googleapis/gapic-generator-python/compare/0.25.0...v0.25.1) (2020-06-23)


### Bug Fixes

* only require dataclases if python<3.7 ([#475](https://www.github.com/googleapis/gapic-generator-python/issues/475)) ([9597695](https://www.github.com/googleapis/gapic-generator-python/commit/959769518ea47df383b23b6e48c5da148f69029e))

## [0.25.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.24.2...v0.25.0) (2020-06-17)


### Features

* provide AsyncIO support for generated code ([#365](https://www.github.com/googleapis/gapic-generator-python/issues/365)) ([305ed34](https://www.github.com/googleapis/gapic-generator-python/commit/305ed34cfc1607c990f2f88b27f53358da25c366))

### [0.24.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.24.1...v0.24.2) (2020-06-13)


### Bug Fixes

* generated unit tests live in the 'tests/gapic' subdir ([#456](https://www.github.com/googleapis/gapic-generator-python/issues/456)) ([1ed7c9d](https://www.github.com/googleapis/gapic-generator-python/commit/1ed7c9d6fe9595c390387d72113d741ebf28538d)), closes [#454](https://www.github.com/googleapis/gapic-generator-python/issues/454)

### [0.24.1](https://www.github.com/googleapis/gapic-generator-python/compare/0.24.0...v0.24.1) (2020-06-12)


### Bug Fixes

* update GOOGLE_API_USE_MTLS value ([#453](https://www.github.com/googleapis/gapic-generator-python/issues/453)) ([7449ad5](https://www.github.com/googleapis/gapic-generator-python/commit/7449ad5aad4a1fbbf9ca3796e097512fc80991e3))
