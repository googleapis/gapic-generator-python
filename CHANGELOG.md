# Changelog

### [0.39.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.39.0...v0.39.1) (2021-01-05)


### Bug Fixes

* fix missing .coveragerc and the broken bazel build ([#723](https://www.github.com/googleapis/gapic-generator-python/issues/723)) ([7f8235f](https://www.github.com/googleapis/gapic-generator-python/commit/7f8235f6dfbd309a879895701aeb5e73c6425483))
* Update gapic-generator-python to gracefully handle internal google inconsistencies ([#721](https://www.github.com/googleapis/gapic-generator-python/issues/721)) ([b984295](https://www.github.com/googleapis/gapic-generator-python/commit/b9842952433924a1d8de4ef9cc3ea9e7fa91c01a))
* updating testing, rest-only generation, & minor bug-fixes ([#716](https://www.github.com/googleapis/gapic-generator-python/issues/716)) ([56c31de](https://www.github.com/googleapis/gapic-generator-python/commit/56c31de4a9f661e3d69b52e19c9a28dddfe9d7dc))

## [0.39.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.38.0...v0.39.0) (2020-12-22)


### Features

* allow warehouse name to be customized ([#717](https://www.github.com/googleapis/gapic-generator-python/issues/717)) ([7c185e8](https://www.github.com/googleapis/gapic-generator-python/commit/7c185e87cb4252b1f99ed121515814595f9492c4)), closes [#605](https://www.github.com/googleapis/gapic-generator-python/issues/605)


### Bug Fixes

* fix sphinx identifiers ([#714](https://www.github.com/googleapis/gapic-generator-python/issues/714)) ([39be474](https://www.github.com/googleapis/gapic-generator-python/commit/39be474b4419dfa521ef51927fd36dbf257d68e3)), closes [#625](https://www.github.com/googleapis/gapic-generator-python/issues/625) [#604](https://www.github.com/googleapis/gapic-generator-python/issues/604)

## [0.38.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.37.1...v0.38.0) (2020-12-16)


### Features

* add 'from_service_account_info' factory to clients ([#706](https://www.github.com/googleapis/gapic-generator-python/issues/706)) ([94d5f0c](https://www.github.com/googleapis/gapic-generator-python/commit/94d5f0c11b8041cbae8e4a89bb504d6c6e200a95)), closes [#705](https://www.github.com/googleapis/gapic-generator-python/issues/705)

### [0.37.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.37.0...v0.37.1) (2020-12-10)


### Bug Fixes

* remove client recv msg limit ([#704](https://www.github.com/googleapis/gapic-generator-python/issues/704)) ([80147ce](https://www.github.com/googleapis/gapic-generator-python/commit/80147ce177ce435dcb1b611181e80dc35f915293))

## [0.37.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.36.0...v0.37.0) (2020-12-08)


### Features

* add proper handling of query/path/body parameters for rest transport ([#702](https://www.github.com/googleapis/gapic-generator-python/issues/702)) ([6b2de5d](https://www.github.com/googleapis/gapic-generator-python/commit/6b2de5dd9fbf15e6b0a42b428b01eb03f1a3820a))

## [0.36.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.11...v0.36.0) (2020-11-14)


### Features

* add rest transport generation for clients with optional transport flag ([#688](https://www.github.com/googleapis/gapic-generator-python/issues/688)) ([af59c2c](https://www.github.com/googleapis/gapic-generator-python/commit/af59c2c3c3d6b7e1f626c3fbc2c03f99ca31b4a4))

### [0.35.11](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.10...v0.35.11) (2020-11-12)


### Bug Fixes

* add enums to types/__init__.py ([#695](https://www.github.com/googleapis/gapic-generator-python/issues/695)) ([e1d4a4a](https://www.github.com/googleapis/gapic-generator-python/commit/e1d4a4ae768a631f6e6dc28f2acfde8be8dc4a8f))
* update protobuf version [gapic-generator-python] ([#696](https://www.github.com/googleapis/gapic-generator-python/issues/696)) ([ea3e519](https://www.github.com/googleapis/gapic-generator-python/commit/ea3e5198862881f5b142638df6ea604654f81f82))

### [0.35.10](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.9...v0.35.10) (2020-11-09)


### Documentation

* fix a few typos ([#690](https://www.github.com/googleapis/gapic-generator-python/issues/690)) ([2716838](https://www.github.com/googleapis/gapic-generator-python/commit/2716838fb739c9350eee2c95b5cf207c4d83423d))

### [0.35.9](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.8...v0.35.9) (2020-10-27)


### Performance Improvements

* collisions don't contain reserved names by default ([#684](https://www.github.com/googleapis/gapic-generator-python/issues/684)) ([2ec6ea6](https://www.github.com/googleapis/gapic-generator-python/commit/2ec6ea6835256c0d7b252e035cf4eac1ff442647))

### [0.35.8](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.7...v0.35.8) (2020-10-21)


### Documentation

* generated message types reference proto-plus ([#680](https://www.github.com/googleapis/gapic-generator-python/issues/680)) ([23327b2](https://www.github.com/googleapis/gapic-generator-python/commit/23327b275fb5a3fefe6c47cb15b9d9ecb02aac1f))

### [0.35.7](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.6...v0.35.7) (2020-10-21)


### Bug Fixes

* expose ssl credentials from transport ([#677](https://www.github.com/googleapis/gapic-generator-python/issues/677)) ([da0ee3e](https://www.github.com/googleapis/gapic-generator-python/commit/da0ee3eab4f80bf3d70fa5e06a2dcef7e1d4d22e))

### [0.35.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.5...v0.35.6) (2020-10-20)


### Bug Fixes

* unknown resources do not cause a generator crash ([#675](https://www.github.com/googleapis/gapic-generator-python/issues/675)) ([2d23d7d](https://www.github.com/googleapis/gapic-generator-python/commit/2d23d7d202099ccf145c01aeb9a03ae46b4e1b00))

### [0.35.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.4...v0.35.5) (2020-10-19)


### Bug Fixes

* numerous small fixes to allow bigtable-admin ([#660](https://www.github.com/googleapis/gapic-generator-python/issues/660)) ([09692c4](https://www.github.com/googleapis/gapic-generator-python/commit/09692c4e889ccde3b0ca31a5e8476c1679804beb))

### [0.35.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.3...v0.35.4) (2020-10-16)


### Bug Fixes

* minor typo in ads template ([#664](https://www.github.com/googleapis/gapic-generator-python/issues/664)) ([816f965](https://www.github.com/googleapis/gapic-generator-python/commit/816f965c8560bf65d8043bd67672c660a2b1300b))

### [0.35.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.2...v0.35.3) (2020-10-13)


### Documentation

* remove references to pipsi ([#656](https://www.github.com/googleapis/gapic-generator-python/issues/656)) ([39c612b](https://www.github.com/googleapis/gapic-generator-python/commit/39c612b545bc93c7c738a78f074672ee66365efb))

### [0.35.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.1...v0.35.2) (2020-10-13)


### Bug Fixes

* modules referenced in MapField message type are properly aliased ([#654](https://www.github.com/googleapis/gapic-generator-python/issues/654)) ([2c79349](https://www.github.com/googleapis/gapic-generator-python/commit/2c79349e7b89435bc45e499885f7b12ac0bc2d9f)), closes [#618](https://www.github.com/googleapis/gapic-generator-python/issues/618)

### [0.35.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.35.0...v0.35.1) (2020-10-09)


### Bug Fixes

* the common resources are not targets for lookup ([#650](https://www.github.com/googleapis/gapic-generator-python/issues/650)) ([8e1b384](https://www.github.com/googleapis/gapic-generator-python/commit/8e1b384e812ef519c421c8c288d5118961d8b4cf))

## [0.35.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.4...v0.35.0) (2020-10-09)


### Features

* file_level and indirectly used resources generate helper methods ([#642](https://www.github.com/googleapis/gapic-generator-python/issues/642)) ([42e224c](https://www.github.com/googleapis/gapic-generator-python/commit/42e224cb100f6e2aa9370bc6a5179d62979b5c4d)), closes [#637](https://www.github.com/googleapis/gapic-generator-python/issues/637)

### [0.34.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.3...v0.34.4) (2020-10-09)


### Bug Fixes

* expose transport property for clients ([#645](https://www.github.com/googleapis/gapic-generator-python/issues/645)) ([13cddda](https://www.github.com/googleapis/gapic-generator-python/commit/13cddda0623bd4d24ae7973752b1be0eaa40523a)), closes [#640](https://www.github.com/googleapis/gapic-generator-python/issues/640)

### [0.34.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.2...v0.34.3) (2020-10-08)


### Bug Fixes

* fix types on server and bidi streaming callables ([#641](https://www.github.com/googleapis/gapic-generator-python/issues/641)) ([d92c202](https://www.github.com/googleapis/gapic-generator-python/commit/d92c2029398c969ebf2a68a5bf77c5eb4fff7b31))

### [0.34.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.1...v0.34.2) (2020-09-30)


### Bug Fixes

* resource messages in method response types generate helpers ([#629](https://www.github.com/googleapis/gapic-generator-python/issues/629)) ([52bfd6d](https://www.github.com/googleapis/gapic-generator-python/commit/52bfd6d5d5821b33e78e6b9867a3be2865cdbc74))

### [0.34.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.34.0...v0.34.1) (2020-09-30)


### Bug Fixes

* fix typo attribue -> attribute ([#627](https://www.github.com/googleapis/gapic-generator-python/issues/627)) ([729146f](https://www.github.com/googleapis/gapic-generator-python/commit/729146fd53edf1e4ae4d3c9a90640a7520b1ba9d)), closes [#626](https://www.github.com/googleapis/gapic-generator-python/issues/626)

## [0.34.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.8...v0.34.0) (2020-09-29)


### Features

* add support for common resource paths ([#622](https://www.github.com/googleapis/gapic-generator-python/issues/622)) ([15a7fde](https://www.github.com/googleapis/gapic-generator-python/commit/15a7fdeb966cb64a742b6305d2c71dd3d485d0f9))

### [0.33.8](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.7...v0.33.8) (2020-09-25)


### Bug Fixes

* handle repeated fields in method signatures ([#445](https://www.github.com/googleapis/gapic-generator-python/issues/445)) ([3aae799](https://www.github.com/googleapis/gapic-generator-python/commit/3aae799f62a1f5d3b0506d919cc6080ee417f14b))

### [0.33.7](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.6...v0.33.7) (2020-09-24)


### Bug Fixes

* retriable exceptions are deterministically ordered in GAPICs ([#619](https://www.github.com/googleapis/gapic-generator-python/issues/619)) ([f7b1164](https://www.github.com/googleapis/gapic-generator-python/commit/f7b11640b74d8c64747b33783976d6e0ab9c61c4))

### [0.33.6](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.5...v0.33.6) (2020-09-22)


### Bug Fixes

* operation module is properly aliased if necessary ([#615](https://www.github.com/googleapis/gapic-generator-python/issues/615)) ([8f92fd9](https://www.github.com/googleapis/gapic-generator-python/commit/8f92fd9999286ef3f916119be78dbeb838a15550)), closes [#610](https://www.github.com/googleapis/gapic-generator-python/issues/610)

### [0.33.5](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.4...v0.33.5) (2020-09-22)


### Bug Fixes

* remove 'property' from reserved names ([#613](https://www.github.com/googleapis/gapic-generator-python/issues/613)) ([8338a51](https://www.github.com/googleapis/gapic-generator-python/commit/8338a51a81f5f5b8ebacf68c8e46d3e1804d3f8b))

### [0.33.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.3...v0.33.4) (2020-09-17)


### Bug Fixes

* 'id' should not be a reserved name ([#602](https://www.github.com/googleapis/gapic-generator-python/issues/602)) ([c43c574](https://www.github.com/googleapis/gapic-generator-python/commit/c43c5740db099be19c5f6e52b3a917a631003411))

### [0.33.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.2...v0.33.3) (2020-09-15)


### Bug Fixes

* module names can no longer collide with keywords or builtins ([#595](https://www.github.com/googleapis/gapic-generator-python/issues/595)) ([960d550](https://www.github.com/googleapis/gapic-generator-python/commit/960d550c4a8fd09b052cce785d76243a5d4525d7))

### [0.33.2](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.1...v0.33.2) (2020-09-15)


### Bug Fixes

* ignore types for imports generated from 'google.api_core' ([#597](https://www.github.com/googleapis/gapic-generator-python/issues/597)) ([8440e09](https://www.github.com/googleapis/gapic-generator-python/commit/8440e09855d399d647b62238a9697e04ea4d0d41)), closes [#596](https://www.github.com/googleapis/gapic-generator-python/issues/596)

### [0.33.1](https://www.github.com/googleapis/gapic-generator-python/compare/v0.33.0...v0.33.1) (2020-09-15)


### Bug Fixes

* Fix client template type hints ([#593](https://www.github.com/googleapis/gapic-generator-python/issues/593)) ([93f34e8](https://www.github.com/googleapis/gapic-generator-python/commit/93f34e8a2a351a24a49424c1722baec2893dc764))

## [0.33.0](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.4...v0.33.0) (2020-09-10)


### Features

* support mtls env variables ([#589](https://www.github.com/googleapis/gapic-generator-python/issues/589)) ([b19026d](https://www.github.com/googleapis/gapic-generator-python/commit/b19026d9cca26ebd1cd0c3e73f738c4d1870d987))

### [0.32.4](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.3...v0.32.4) (2020-09-03)


### Bug Fixes

* rendering mock values for recursive messages no longer crashes ([#587](https://www.github.com/googleapis/gapic-generator-python/issues/587)) ([c2a83e5](https://www.github.com/googleapis/gapic-generator-python/commit/c2a83e561bf46b4af21e9008c7d67a1c609d7d06))

### [0.32.3](https://www.github.com/googleapis/gapic-generator-python/compare/v0.32.2...v0.32.3) (2020-08-28)


### Bug Fixes

* stabilize the order of resource helper methods and ([#582](https://www.github.com/googleapis/gapic-generator-python/issues/582)) ([7d2adde](https://www.github.com/googleapis/gapic-generator-python/commit/7d2adde3a1ae81ac88ced822d6dfdfb26ffbfdf0))

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
