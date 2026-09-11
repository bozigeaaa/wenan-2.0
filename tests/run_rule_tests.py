from pathlib import Path
import runpy
import unittest


TEST_ROOT = Path(__file__).resolve().parent
REQUIRED_TEST_FILES = {
    "test_company_soft_placement_rules.py",
    "test_core_writing_framework.py",
    "test_expression_craft_rules.py",
    "test_global_company_product_content_rules.py",
    "test_humanizer_output_rules.py",
    "test_local_delivery_rules.py",
    "test_news_source_flow_rules.py",
    "test_semantic_promise_rules.py",
    "test_structure_health.py",
    "test_title_flow_rules.py",
    "test_triggered_generation_pipeline.py",
}


def main() -> None:
    failures: list[tuple[str, BaseException]] = []
    total = 0
    test_paths = sorted(TEST_ROOT.glob("test_*.py"))
    discovered_files = {path.name for path in test_paths}
    missing_files = sorted(REQUIRED_TEST_FILES - discovered_files)
    if missing_files:
        print(f"FAIL missing required test files: {', '.join(missing_files)}")
        raise SystemExit(1)

    for path in test_paths:
        namespace = runpy.run_path(str(path))
        test_names = [
            name
            for name, candidate in sorted(namespace.items())
            if name.startswith("test_") and callable(candidate)
        ]
        test_classes = [
            candidate for candidate in namespace.values()
            if isinstance(candidate, type) and issubclass(candidate, unittest.TestCase)
            and candidate is not unittest.TestCase
        ]
        if test_classes:
            suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(cls)
                                       for cls in test_classes)
            result = unittest.TestResult()
            suite.run(result)
            total += result.testsRun
            failures.extend((str(test), AssertionError(detail))
                            for test, detail in result.failures + result.errors)
        if not test_names and not test_classes:
            print(f"FAIL {path.name} has no test functions")
            raise SystemExit(1)

        for name in test_names:
            total += 1
            try:
                namespace[name]()
            except BaseException as exc:
                failures.append((f"{path.name}::{name}", exc))

    if total == 0:
        print("FAIL No test functions discovered")
        raise SystemExit(1)

    for name, exc in failures:
        print(f"FAIL {name}: {exc}")

    passed = total - len(failures)
    print(f"{passed} passed, {len(failures)} failed")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
