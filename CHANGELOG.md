# [4.0.0](https://github.com/johnnymillergh/muscle-and-fitness-server/compare/3.0.0...4.0.0) (2022-09-18)


### Features

* **$async:** support decorate function with `@async_function` ([44a0a7e](https://github.com/johnnymillergh/python_boilerplate/commit/44a0a7eaf5ecf68ff0b8e170c0cb7c9c836b1fa9))
* **$flake8:** add more code constraints ([b978b9b](https://github.com/johnnymillergh/python_boilerplate/commit/b978b9b0d43dfb84ccc9e48b5ed51094baf531a6))
* **$GitHooks:** add more hooks for pre-commit ([5114647](https://github.com/johnnymillergh/python_boilerplate/commit/5114647115151d74f68f3855281487e753899215))
* **$loguru:** display process id in log ([5a0177b](https://github.com/johnnymillergh/python_boilerplate/commit/5a0177b6517ea64e296d855057e35f91c028d4ab))
* **$pandas:** add usage example of using pandas DataFrame to generate CSV ([161c7ba](https://github.com/johnnymillergh/python_boilerplate/commit/161c7bae5f0c95fc9e4d888cb2721567251cff09))
* **$pandas:** multiple conditions filter ([b25b7a6](https://github.com/johnnymillergh/python_boilerplate/commit/b25b7a63d755d8412023d03daf0c47b4eaab2bb1))
* move all artifacts under `build` directory ([50e6c46](https://github.com/johnnymillergh/python_boilerplate/commit/50e6c46b8d3ff5303aaf17b8b0a93a3391addf11))


### Performance Improvements

* **$profiling:** replace process_time() -> perf_counter() ([99ca066](https://github.com/johnnymillergh/python_boilerplate/commit/99ca066915c76498394fcbb90d50295577b98c16))
* **$profiling:** user `process_time()` for time profiling ([a55a4c7](https://github.com/johnnymillergh/python_boilerplate/commit/a55a4c7583f319a89626e18972bd0c0e1436c2fa))
* **$pytest:** distribute tests across multiple CPUs to speed up test execution ([b16b2db](https://github.com/johnnymillergh/python_boilerplate/commit/b16b2db587e99c1f253dd351218e42d4d60f17fd))



# [3.0.0](https://github.com/johnnymillergh/muscle-and-fitness-server/compare/2.0.0...3.0.0) (2022-09-06)


### Features

* **$loguru:** add level icon for log ([4e1cb15](https://github.com/johnnymillergh/python_boilerplate/commit/4e1cb159173ca370161450fbd898c4c71c547570))
* **$loguru:** change data output directory ([06ff16f](https://github.com/johnnymillergh/python_boilerplate/commit/06ff16f77388a4ab5081163066baf1dacc6967a6))
* **$loguru:** correct function reference for log ([11fbddc](https://github.com/johnnymillergh/python_boilerplate/commit/11fbddcfb3239ba7a701d32abdf55062a910035c))
* **$Loguru:** log file with hostname ([ab378b0](https://github.com/johnnymillergh/python_boilerplate/commit/ab378b07bf5edc3a6388ac1c15deeb1cfeaa672e))
* **$Loguru:** log more details for exception ([af5260b](https://github.com/johnnymillergh/python_boilerplate/commit/af5260b9c40e1d3a464e53d85e407edafca9ce25))
* **$pandas:** integrate matplotlib; filter Sony's game ([2a7d993](https://github.com/johnnymillergh/python_boilerplate/commit/2a7d9930b6f4356494adf7d24391aa08c3c3835a))
* **$peewee:** auto-register table by `@peewee` decorator ([ecd0cde](https://github.com/johnnymillergh/python_boilerplate/commit/ecd0cdedec526136e8f259514037d2553cbf3f28))
* **$profile:** sort profile HTML by original Python package ([5e7a651](https://github.com/johnnymillergh/python_boilerplate/commit/5e7a651a6934ccfad034326d4f130c134e5d357c))
* **$pytest:** integrate pyinstrument to profile test cases ([513d456](https://github.com/johnnymillergh/python_boilerplate/commit/513d4569a70baa8a02741e633f4b9ea5be339156))
* **$SQLite:** retain logs before the program exits ([f310130](https://github.com/johnnymillergh/python_boilerplate/commit/f310130a79be9f392332017f4186c4957f8d15cf))
* **$startup:** record current user and command line when startup ([8ed5022](https://github.com/johnnymillergh/python_boilerplate/commit/8ed5022f66440b3e2f5d37372117dabf2cedc9b5))
* **$Tenacity:** integrate Python retry library with Tenacity ([edff79a](https://github.com/johnnymillergh/python_boilerplate/commit/edff79aa5a492ef9a017e24e5d752cd0f05ec1c3))
* **$trace:** support function calling trace with SQLite persistence ([3b3b57a](https://github.com/johnnymillergh/python_boilerplate/commit/3b3b57a39d986772bdf97518efa630c8ef77a96c))
* record current user and host name ([7602d50](https://github.com/johnnymillergh/python_boilerplate/commit/7602d50277c6e0e329a7d8134496d2db1e0fc394))


### Performance Improvements

* **$Path:** use object-oriented filesystem paths ([d67cce1](https://github.com/johnnymillergh/python_boilerplate/commit/d67cce1a057df059d4e8768f7530169147e0f0f6))
* **$SQLite:** use recommended setting for SQLite ([dc4274d](https://github.com/johnnymillergh/python_boilerplate/commit/dc4274d6918151a8067357e5785fe991e3273450))
* profile pytest UT with pyinstrument ([ba55445](https://github.com/johnnymillergh/python_boilerplate/commit/ba554458824c6acbcc646750b7f2be0f7c3ad808))



# [2.0.0](https://github.com/johnnymillergh/muscle-and-fitness-server/compare/1.0.0...2.0.0) (2022-08-28)


### Performance Improvements

* refactored by latest dependencies ([4c6bd41](https://github.com/johnnymillergh/python_boilerplate/commit/4c6bd416e3afbd3c709ceac0edc1c8cf7dfa13bc))



# 1.0.0 (2021-11-06)


### Features

* **$Mail:** support sending email ([1ed261b](https://github.com/johnnymillergh/python_boilerplate/commit/1ed261b38de4319c056f48dbbf115ca175edc890))
