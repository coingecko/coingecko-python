# Changelog

## 2.0.2 (2026-05-01)

Full Changelog: [v2.0.1...v2.0.2](https://github.com/coingecko/coingecko-python/compare/v2.0.1...v2.0.2)

### Chores

* **internal:** reformat pyproject.toml ([f32c0f3](https://github.com/coingecko/coingecko-python/commit/f32c0f3d2e71c274c00f2b5e9608be42c5e5169b))

## 2.0.1 (2026-04-30)

Full Changelog: [v2.0.0...v2.0.1](https://github.com/coingecko/coingecko-python/compare/v2.0.0...v2.0.1)

### Bug Fixes

* Remove orphaned MCP tools ([f85b4af](https://github.com/coingecko/coingecko-python/commit/f85b4af2fbddd5e30ba43f658f56ccf49c245239))

## 2.0.0 (2026-04-30)

Full Changelog: [v1.14.2...v2.0.0](https://github.com/coingecko/coingecko-python/compare/v1.14.2...v2.0.0)

### ⚠ BREAKING CHANGES

* AIP updates; fix!: Pydantic response model

### Features

* AIP updates; fix!: Pydantic response model ([8c4629e](https://github.com/coingecko/coingecko-python/commit/8c4629e7c7431cc8925b757fd23c205816357ed6))
* support setting headers via env ([3979340](https://github.com/coingecko/coingecko-python/commit/3979340037d5ec65908c8c9e8d21d67e6e770ae8))


### Bug Fixes

* use correct field name format for multipart file arrays ([5932ae6](https://github.com/coingecko/coingecko-python/commit/5932ae6d020e9841a92773aee20ea926b849945e))


### Chores

* **internal:** more robust bootstrap script ([e53a0fc](https://github.com/coingecko/coingecko-python/commit/e53a0fc7939c399537fefd1cf9d77044a1925c94))

## 1.14.2 (2026-04-18)

Full Changelog: [v1.14.1...v1.14.2](https://github.com/coingecko/coingecko-python/compare/v1.14.1...v1.14.2)

### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([e5d3b21](https://github.com/coingecko/coingecko-python/commit/e5d3b21f3760652cf307989dade7a93bffe10811))

## 1.14.1 (2026-04-11)

Full Changelog: [v1.14.0...v1.14.1](https://github.com/coingecko/coingecko-python/compare/v1.14.0...v1.14.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([ffefe0c](https://github.com/coingecko/coingecko-python/commit/ffefe0c8418ab5f77790f3c21dbd78157879c629))
* ensure file data are only sent as 1 parameter ([7b09afe](https://github.com/coingecko/coingecko-python/commit/7b09afe02609030c9da627e2f3475063652a254a))

## 1.14.0 (2026-03-27)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/coingecko/coingecko-python/compare/v1.13.0...v1.14.0)

### Features

* **internal:** implement indices array format for query and form serialization ([6b672e3](https://github.com/coingecko/coingecko-python/commit/6b672e393231b592ae0ec3d7aec8a41aab5ce331))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([7a2809e](https://github.com/coingecko/coingecko-python/commit/7a2809e203ebeacd52704696b19c94780d9c0db6))
* **pydantic:** do not pass `by_alias` unless set ([5b4c5d1](https://github.com/coingecko/coingecko-python/commit/5b4c5d1fec42630e39a569422baf75eb0990bb31))
* sanitize endpoint path params ([a87e9d4](https://github.com/coingecko/coingecko-python/commit/a87e9d4bacf39d06c9becdd45dcf6a422699e987))


### Chores

* **ci:** skip lint on metadata-only changes ([07969b0](https://github.com/coingecko/coingecko-python/commit/07969b071692db08955e6dec6d1c85ef751e2cf5))
* **ci:** skip uploading artifacts on stainless-internal branches ([53e9338](https://github.com/coingecko/coingecko-python/commit/53e93380ab1adfadf0a86d219c9216bb8bfe4174))
* **internal:** tweak CI branches ([4d1960a](https://github.com/coingecko/coingecko-python/commit/4d1960abd7dfb3610749bcc303579deb787f8853))
* **internal:** update gitignore ([5266e41](https://github.com/coingecko/coingecko-python/commit/5266e41274a94efa377aa80cd77f67e0f2369311))

## 1.13.0 (2026-02-25)

Full Changelog: [v1.12.0...v1.13.0](https://github.com/coingecko/coingecko-python/compare/v1.12.0...v1.13.0)

### Features

* **api:** api update ([0241244](https://github.com/coingecko/coingecko-python/commit/02412444ad3bbc58bbec8f16c4e3e18d84ac3969))
* **api:** api update ([8436976](https://github.com/coingecko/coingecko-python/commit/84369760ef357df8e4feb0285263b7896d081948))
* **client:** add custom JSON encoder for extended type support ([dad7856](https://github.com/coingecko/coingecko-python/commit/dad7856f521034641be1af22a9de396d5b3816ff))
* **client:** add support for binary request streaming ([a9f1aa3](https://github.com/coingecko/coingecko-python/commit/a9f1aa33c8765610d03550e5721b0279d172d273))
* **client:** support file upload requests ([9d2d8ee](https://github.com/coingecko/coingecko-python/commit/9d2d8ee494cfaf60ed0bcc9a7b6b4e7b0cff30d5))


### Bug Fixes

* **client:** loosen auth header validation ([eafba80](https://github.com/coingecko/coingecko-python/commit/eafba8079e34ec10de0153950de8d6637c1d422a))
* **docs:** fix mcp installation instructions for remote servers ([62c08fb](https://github.com/coingecko/coingecko-python/commit/62c08fb291eab975560ce0d0e055a5b88fc7029d))


### Chores

* **ci:** upgrade `actions/github-script` ([4e83c98](https://github.com/coingecko/coingecko-python/commit/4e83c9866f46c4f1b695ac83e566e5d04fdbea77))
* format all `api.md` files ([94bf810](https://github.com/coingecko/coingecko-python/commit/94bf810205db49812c2bbbe25f3018a2ac228170))
* **internal:** add `--fix` argument to lint script ([0a4e127](https://github.com/coingecko/coingecko-python/commit/0a4e127596bee226b220890acc706e6782d553ab))
* **internal:** bump dependencies ([369ba5d](https://github.com/coingecko/coingecko-python/commit/369ba5d99e285c3ac88ef80c193c7563769c36be))
* **internal:** codegen related update ([cc420eb](https://github.com/coingecko/coingecko-python/commit/cc420ebc39f9ab254ef2be16bf065fc513fcd2d3))
* **internal:** fix lint error on Python 3.14 ([9134bbc](https://github.com/coingecko/coingecko-python/commit/9134bbc5b7ca8c752e677aec2eb84fc1b627409f))
* **internal:** update `actions/checkout` version ([f633c5e](https://github.com/coingecko/coingecko-python/commit/f633c5ef5aa1daf0ce6c05efd058571099e1cc06))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([10cb284](https://github.com/coingecko/coingecko-python/commit/10cb284cf8300229a26c6816a737ba772870d7aa))

## 1.12.0 (2025-12-18)

Full Changelog: [v1.11.3...v1.12.0](https://github.com/coingecko/coingecko-python/compare/v1.11.3...v1.12.0)

### Features

* **api:** api update ([e0bf518](https://github.com/coingecko/coingecko-python/commit/e0bf5186eaaf4a10315c162e71f40a1c7c8bfffc))
* **api:** manual updates ([9a717af](https://github.com/coingecko/coingecko-python/commit/9a717af9715da994018f8fbb9b3199e1bf3929ad))

## 1.11.3 (2025-12-18)

Full Changelog: [v1.11.2...v1.11.3](https://github.com/coingecko/coingecko-python/compare/v1.11.2...v1.11.3)

### Bug Fixes

* ensure streams are always closed ([e51d469](https://github.com/coingecko/coingecko-python/commit/e51d46991166ae87d5dadd827f803ce0f293ea88))
* Remove incorrect comment ([12a638c](https://github.com/coingecko/coingecko-python/commit/12a638cc2b314240ea9c5ddf460bfab88542b797))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([dfe9c19](https://github.com/coingecko/coingecko-python/commit/dfe9c19b68627e99139837f8b00b2d35948e2e87))
* use async_to_httpx_files in patch method ([6482e2b](https://github.com/coingecko/coingecko-python/commit/6482e2b102a82dbea5f8f6951af0ba0809d3b4b0))


### Chores

* add missing docstrings ([d90bf87](https://github.com/coingecko/coingecko-python/commit/d90bf87cc6149e32d10bbb81f5d12a97fbc14eb9))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([4fb9fd2](https://github.com/coingecko/coingecko-python/commit/4fb9fd29b779f96b3fa57bba750afbcbcd70e06b))
* **docs:** use environment variables for authentication in code snippets ([cd2478b](https://github.com/coingecko/coingecko-python/commit/cd2478b3aa36989a4685cab291eeae5cc7521c39))
* **internal:** add missing files argument to base client ([fdfb733](https://github.com/coingecko/coingecko-python/commit/fdfb733c0826445d3cac26ac220335c19df07a94))
* speedup initial import ([41bfc15](https://github.com/coingecko/coingecko-python/commit/41bfc1506a5ef1ffe945dbdc9996f12dd425a34d))
* update lockfile ([def90a4](https://github.com/coingecko/coingecko-python/commit/def90a462f594215307855a485fb0defb2e59f21))

## 1.11.2 (2025-11-22)

Full Changelog: [v1.11.1...v1.11.2](https://github.com/coingecko/coingecko-python/compare/v1.11.1...v1.11.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([920e115](https://github.com/coingecko/coingecko-python/commit/920e115252ab911ed3e0f0f588efd3302eb07651))
* compat with Python 3.14 ([480f678](https://github.com/coingecko/coingecko-python/commit/480f67880356efaff1bc290881d64b010f775c54))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([c8703be](https://github.com/coingecko/coingecko-python/commit/c8703be34335b1dc7cca5f8e6c00267babd95bfd))


### Chores

* add Python 3.14 classifier and testing ([aa3cd7d](https://github.com/coingecko/coingecko-python/commit/aa3cd7d3a3c4d8d202726cc1b617ed05bacbb8d2))
* bump `httpx-aiohttp` version to 0.1.9 ([8bb3482](https://github.com/coingecko/coingecko-python/commit/8bb3482e800e3b28a107bf2d71e888cad9e16855))
* **internal/tests:** avoid race condition with implicit client cleanup ([21f1918](https://github.com/coingecko/coingecko-python/commit/21f1918d6dd982b0bf0280cd5585cfdab8d1e275))
* **internal:** detect missing future annotations with ruff ([c7100fb](https://github.com/coingecko/coingecko-python/commit/c7100fb15194c4eb34d12cb995ea2a81ebfe0b26))
* **internal:** grammar fix (it's -&gt; its) ([10ceb55](https://github.com/coingecko/coingecko-python/commit/10ceb55cfbb9ee6dbd27a9d8e02fd302005c7f70))
* **package:** drop Python 3.8 support ([a8ce8c0](https://github.com/coingecko/coingecko-python/commit/a8ce8c038065a5aecadd21dbf66b8408a3350f1b))

## 1.11.1 (2025-10-06)

Full Changelog: [v1.11.0...v1.11.1](https://github.com/coingecko/coingecko-python/compare/v1.11.0...v1.11.1)

### Bug Fixes

* Incorrect snippet in ReadMe ([d956a5c](https://github.com/coingecko/coingecko-python/commit/d956a5cd13af9fcc5711fc5e3698cf100ac7142a))

## 1.11.0 (2025-10-06)

Full Changelog: [v1.10.1...v1.11.0](https://github.com/coingecko/coingecko-python/compare/v1.10.1...v1.11.0)

### Features

* **api:** api update ([384c417](https://github.com/coingecko/coingecko-python/commit/384c4173d02da6ee84c5650ded6c56530a960fd1))

## 1.10.1 (2025-09-25)

Full Changelog: [v1.10.0...v1.10.1](https://github.com/coingecko/coingecko-python/compare/v1.10.0...v1.10.1)

### Bug Fixes

* Correct accessing example in README ([7a8c9fd](https://github.com/coingecko/coingecko-python/commit/7a8c9fd3c281c92b3946d6f8e4a46566f88ef810))

## 1.10.0 (2025-09-22)

Full Changelog: [v1.9.0...v1.10.0](https://github.com/coingecko/coingecko-python/compare/v1.9.0...v1.10.0)

### Features

* **api:** api update ([ff4a499](https://github.com/coingecko/coingecko-python/commit/ff4a499d348e5312d6eaad322a03cd606478ca58))


### Bug Fixes

* Merge public_treasury config ([a6738ba](https://github.com/coingecko/coingecko-python/commit/a6738ba71c6ead0e662145d7a275d03588be5a9d))
* Stainless config to match the latest endpoints ([73ec25c](https://github.com/coingecko/coingecko-python/commit/73ec25cf0d14fd24a480748c6d5ecfd789005506))

## 1.9.0 (2025-09-20)

Full Changelog: [v1.8.3...v1.9.0](https://github.com/coingecko/coingecko-python/compare/v1.8.3...v1.9.0)

### Features

* improve future compat with pydantic v3 ([a6ad7f5](https://github.com/coingecko/coingecko-python/commit/a6ad7f5bda8eb378eb34f2d65e1c62158df65e91))
* **types:** replace List[str] with SequenceNotStr in params ([fe41e4f](https://github.com/coingecko/coingecko-python/commit/fe41e4f38fd62059691152075d04bad33e4a78f0))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([138163f](https://github.com/coingecko/coingecko-python/commit/138163f74afb1011411f69de7a10f35deb76526a))
* **internal:** move mypy configurations to `pyproject.toml` file ([73f97dc](https://github.com/coingecko/coingecko-python/commit/73f97dc21a268a818948611733fad74958c90a80))
* **internal:** update pydantic dependency ([2db8a2b](https://github.com/coingecko/coingecko-python/commit/2db8a2be8f967ea17557632c98465a8ee2479408))
* **tests:** simplify `get_platform` test ([f344e7e](https://github.com/coingecko/coingecko-python/commit/f344e7ec8a3c5c155adf95cc5890c8a966fb2e19))
* **types:** change optional parameter type from NotGiven to Omit ([4d0a984](https://github.com/coingecko/coingecko-python/commit/4d0a9840a93a259bfe3613cc81443533fa81e7fe))

## 1.8.3 (2025-08-30)

Full Changelog: [v1.8.2...v1.8.3](https://github.com/coingecko/coingecko-python/compare/v1.8.2...v1.8.3)

### Bug Fixes

* avoid newer type syntax ([3533b82](https://github.com/coingecko/coingecko-python/commit/3533b82ee0a7d137c9234e8adcd4bc4cc4b02ffa))


### Chores

* **internal:** add Sequence related utils ([fdf2b29](https://github.com/coingecko/coingecko-python/commit/fdf2b29a17f76d5fe1e7fd33d3d4d0e2350d4362))
* **internal:** change ci workflow machines ([5a910b3](https://github.com/coingecko/coingecko-python/commit/5a910b3be656bff201e854d7aab7fa8093fe7a01))
* **internal:** codegen related update ([73e0df0](https://github.com/coingecko/coingecko-python/commit/73e0df07412c4bf958eb91a7a3d89b3683284237))
* **internal:** update pyright exclude list ([6b0b243](https://github.com/coingecko/coingecko-python/commit/6b0b2431134970e1fef1b572938537c7425bf096))
* update github action ([bd13157](https://github.com/coingecko/coingecko-python/commit/bd13157fd9eb56aefd6c70ab2874d766654cf0cf))

## 1.8.2 (2025-07-25)

Full Changelog: [v1.8.1...v1.8.2](https://github.com/coingecko/coingecko-python/compare/v1.8.1...v1.8.2)

### Bug Fixes

* **parsing:** parse extra field types ([7c699a8](https://github.com/coingecko/coingecko-python/commit/7c699a8cb5c3651cdf1fd329a51c57619d50339f))


### Chores

* **project:** add settings file for vscode ([7896645](https://github.com/coingecko/coingecko-python/commit/7896645442aee75fa284c9a26b65231ef7d4328e))

## 1.8.1 (2025-07-22)

Full Changelog: [v1.8.0...v1.8.1](https://github.com/coingecko/coingecko-python/compare/v1.8.0...v1.8.1)

### Bug Fixes

* **parsing:** ignore empty metadata ([7cb1ba9](https://github.com/coingecko/coingecko-python/commit/7cb1ba9af13b27b34b2f4456d7f2706ecc6d2dd1))

## 1.8.0 (2025-07-20)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/coingecko/coingecko-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** api update ([a54406c](https://github.com/coingecko/coingecko-python/commit/a54406c294216c329cedc334e72673219b0da05b))

## 1.7.0 (2025-07-15)

Full Changelog: [v1.6.1...v1.7.0](https://github.com/coingecko/coingecko-python/compare/v1.6.1...v1.7.0)

### Features

* clean up environment call outs ([f82dc91](https://github.com/coingecko/coingecko-python/commit/f82dc916f6a00151260d27cd2d31c2d6d3ebfd5f))

## 1.6.1 (2025-07-12)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/coingecko/coingecko-python/compare/v1.6.0...v1.6.1)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([8a4fd1d](https://github.com/coingecko/coingecko-python/commit/8a4fd1d567da36aa07c4ee0f1aa15ca007fa82a8))


### Chores

* **readme:** fix version rendering on pypi ([a0dbf14](https://github.com/coingecko/coingecko-python/commit/a0dbf14fddbd7cea8d2fa6f5e9f0c150852236bf))

## 1.6.0 (2025-07-09)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/coingecko/coingecko-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** api update ([e9e6d07](https://github.com/coingecko/coingecko-python/commit/e9e6d07786128ed47006a294158227ad94a4c9b8))

## 1.5.0 (2025-07-09)

Full Changelog: [v1.4.3...v1.5.0](https://github.com/coingecko/coingecko-python/compare/v1.4.3...v1.5.0)

### Features

* **api:** api update ([b41c660](https://github.com/coingecko/coingecko-python/commit/b41c660bac9c294c73b8a86de00df0880dafa01d))


### Chores

* **internal:** bump pinned h11 dep ([13baf6c](https://github.com/coingecko/coingecko-python/commit/13baf6ccd984b531b02c8db73fe068b992169895))
* **package:** mark python 3.13 as supported ([8b2928d](https://github.com/coingecko/coingecko-python/commit/8b2928d3d25fb242e9e06c31c368f968c5926a2f))

## 1.4.3 (2025-07-08)

Full Changelog: [v1.4.2...v1.4.3](https://github.com/coingecko/coingecko-python/compare/v1.4.2...v1.4.3)

### Chores

* **internal:** codegen related update ([248b684](https://github.com/coingecko/coingecko-python/commit/248b68401d0ec618acab47331b28e2b76fd8c4ce))

## 1.4.2 (2025-07-02)

Full Changelog: [v1.4.1...v1.4.2](https://github.com/coingecko/coingecko-python/compare/v1.4.1...v1.4.2)

### Bug Fixes

* **ci:** correct conditional ([7726945](https://github.com/coingecko/coingecko-python/commit/7726945a5743e28a4648e02bf4876f0a1b87f75c))


### Chores

* **ci:** change upload type ([2ef9872](https://github.com/coingecko/coingecko-python/commit/2ef9872675567a711712da5d1d097482898cd68d))

## 1.4.1 (2025-06-28)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/coingecko/coingecko-python/compare/v1.4.0...v1.4.1)

### Bug Fixes

* **ci:** release-doctor — report correct token name ([62a033e](https://github.com/coingecko/coingecko-python/commit/62a033edbd1724b28675b56b93c30f2b08d774f1))


### Chores

* **ci:** only run for pushes and fork pull requests ([5db6eab](https://github.com/coingecko/coingecko-python/commit/5db6eab0f596f4e670280e231707f63ea82688b6))
* **tests:** skip some failing tests on the latest python versions ([f5e4873](https://github.com/coingecko/coingecko-python/commit/f5e487351a37cca5de41139c656a1c48a09bf6ec))

## 1.4.0 (2025-06-23)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/coingecko/coingecko-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([cad480f](https://github.com/coingecko/coingecko-python/commit/cad480ff6c82385a647f9b4f8340e0e16588f7bb))

## 1.3.0 (2025-06-21)

Full Changelog: [v1.2.1...v1.3.0](https://github.com/coingecko/coingecko-python/compare/v1.2.1...v1.3.0)

### Features

* **client:** add support for aiohttp ([f2c6437](https://github.com/coingecko/coingecko-python/commit/f2c64372ad045019cbc51c9f9abf3a9c3df8633e))

## 1.2.1 (2025-06-19)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/coingecko/coingecko-python/compare/v1.2.0...v1.2.1)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([f7d45a8](https://github.com/coingecko/coingecko-python/commit/f7d45a825ab455b05242e396da0dfce74eeed44c))


### Chores

* **ci:** enable for pull requests ([a0ed478](https://github.com/coingecko/coingecko-python/commit/a0ed4785eb7e04cbd2a948f31123f0981020c5eb))
* **internal:** update conftest.py ([12b1700](https://github.com/coingecko/coingecko-python/commit/12b170018f682c36ef7b12c85eb66f368fd7a535))
* **readme:** update badges ([815ee9f](https://github.com/coingecko/coingecko-python/commit/815ee9f4c7a155eca1ef5775e188a9d48f0418ea))
* **tests:** add tests for httpx client instantiation & proxies ([352858a](https://github.com/coingecko/coingecko-python/commit/352858ae3fdb260cb638b23e745c1fb9e06dc6d1))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([1b205fd](https://github.com/coingecko/coingecko-python/commit/1b205fd1bb9ca50eaef4ef5139f5a21f3fb4c655))

## 1.2.0 (2025-06-13)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/coingecko/coingecko-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** manual updates ([7ff4d0d](https://github.com/coingecko/coingecko-python/commit/7ff4d0d6989cc21fcc41f383b0483d45484d14e7))

## 1.1.0 (2025-06-13)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/coingecko/coingecko-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** Update example response ([ea77eac](https://github.com/coingecko/coingecko-python/commit/ea77eacb32e83b5adf9935eae92dc9bbe29e5a69))


### Bug Fixes

* **client:** correctly parse binary response | stream ([7df7dc4](https://github.com/coingecko/coingecko-python/commit/7df7dc4a59b037a167ed63c849c08436aac08bde))


### Chores

* **tests:** run tests in parallel ([115a0dc](https://github.com/coingecko/coingecko-python/commit/115a0dcd97d26d7005a72a47c24c49bc4b0713b3))

## 1.0.1 (2025-06-10)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/coingecko/coingecko-python/compare/v1.0.0...v1.0.1)

### Chores

* **internal:** version bump ([8773836](https://github.com/coingecko/coingecko-python/commit/87738364b7ecbf1c534528067548d5ad75282809))

## 1.0.0 (2025-06-10)

Full Changelog: [v0.1.0-alpha.7...v1.0.0](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.7...v1.0.0)

### Chores

* update SDK settings ([4fd9a80](https://github.com/coingecko/coingecko-python/commit/4fd9a80c750f4de6facf297537ae9bb1b267ceca))

## 0.1.0-alpha.7 (2025-06-08)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** Update to coingecko_sdk ([262a767](https://github.com/coingecko/coingecko-python/commit/262a76703b119bcc2648db0e21a63d9400a8719c))

## 0.1.0-alpha.6 (2025-06-07)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** api update ([9f7378c](https://github.com/coingecko/coingecko-python/commit/9f7378c9775aa51e345033dded23a26e65878b97))
* **api:** New endpoints ([fd3b486](https://github.com/coingecko/coingecko-python/commit/fd3b486f6528d71be7df3a5a9186ace2742819bd))

## 0.1.0-alpha.5 (2025-06-03)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **client:** add follow_redirects request option ([f01e996](https://github.com/coingecko/coingecko-python/commit/f01e99674f5b0e7d243395588ad6a87e88eda894))


### Chores

* **docs:** remove reference to rye shell ([5c72fbf](https://github.com/coingecko/coingecko-python/commit/5c72fbf675d06b2b8ccfd36604d01cc28ad9a637))

## 0.1.0-alpha.4 (2025-06-02)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([0c72a75](https://github.com/coingecko/coingecko-python/commit/0c72a7510464ed2bc0620d1ed64b6ab40f7145b7))

## 0.1.0-alpha.3 (2025-05-29)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([0812f21](https://github.com/coingecko/coingecko-python/commit/0812f2163205be4e48486f201ab979b78593e9a1))

## 0.1.0-alpha.2 (2025-05-28)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/coingecko/coingecko-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([3869350](https://github.com/coingecko/coingecko-python/commit/3869350a197c6e83fe5c68199ea6047bc177cf14))

## 0.1.0-alpha.1 (2025-05-28)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/coingecko/coingecko-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([2b17650](https://github.com/coingecko/coingecko-python/commit/2b17650480b4d839844a1fb09a7a1eba74a48966))
* **api:** update via SDK Studio ([c7b2f6c](https://github.com/coingecko/coingecko-python/commit/c7b2f6c7a949b1ac299601712e291dd22cad5d20))
* **api:** update via SDK Studio ([2e88eda](https://github.com/coingecko/coingecko-python/commit/2e88edae53fe8c78f114d83a069bdcd90e1505ef))


### Chores

* update SDK settings ([616d906](https://github.com/coingecko/coingecko-python/commit/616d9066a6514fb0f9d33dd941a135bcf84700ca))
