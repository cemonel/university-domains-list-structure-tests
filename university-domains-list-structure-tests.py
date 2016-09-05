#!/usr/bin/env python

import json



class TestRunner(object):
    """
    Runs tests for university domains
    """
    def __init__(self, json_path="world_universities_and_domains.json"):
        super(TestRunner, self).__init__()

        self.json_path = json_path
        self.json_data = None

    def run_tests(self):
        if self.preflight():
            if self.test_field_names():
                if self.test_duplicate():
                    print("No error. Test is completed succesfully.")

    def preflight(self):
        try:
            world_universities_and_domains_file = open("world_universities_and_domains.json")
            self.json_data = json.load(world_universities_and_domains_file)
            world_universities_and_domains_file.close()
        except ValueError:
            print("This file is not json")
            return False
        except FileNotFoundError:
            print("File not found")
            return False

        return True

    def test_field_names(self):
        is_valid = True
        for bundle in self.json_data:
            for field in bundle:
                if field in ("country",
                             "name",
                             "domain",
                             "web_page",
                             "alpha_two_code"):
                    pass
                else:
                    print("Test Failed: Field name error in Bundle: \n%s \nField: %s" % (bundle, field))
                    is_valid = False

        return is_valid

    def test_duplicate(self):
        bundles_list = []
        return_value = True
        for bundle in self.json_data:
            bundle_fields = []
            bundle_name = bundle["name"]
            bundle_country = bundle["country"]
            bundle_domain = bundle["domain"]
            bundle_web_page = bundle["web_page"]
            bundle_fields.append(bundle_name)
            bundle_fields.append(bundle_domain)
            bundle_fields.append(bundle_country)
            bundle_fields.append(bundle_web_page)
            if bundle_fields not in bundles_list:
                bundles_list.append(bundle_fields)
            else:
                print("Duplicate bundle Error: %s " % bundle)
                return_value = False

        return return_value

if __name__ == "__main__":
    test_runner = TestRunner()

    test_runner.run_tests()

