import pytest
from playwright.sync_api import Page
from Tests.test_base import TestBase


class CheckListOfServices(TestBase):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        super(CheckListOfServices, self).setup(page, "")

    def test_list_of_services(self):
        self.assert_services()

    def assert_services(self):
        licenced_list_from_server = self.get_e_sources_by_license()
        correct_licenced_list = self.get_correct_list_of_services()
        self.assertEqual(len(correct_licenced_list), len(licenced_list_from_server))
        for correct_e_source in correct_licenced_list:
            self.assertIn(correct_e_source, licenced_list_from_server)

    def get_e_sources_by_license(self):
        licenced_list = []
        for e_source in self.data.e_source_list:
            if e_source.active is 1 and e_source.facet_access == "předplacený (licencovaný)":
                licenced_list.append(e_source.title_display.strip())
        return licenced_list

    def get_correct_list_of_services(self):
        return [
            "Academic Search Complete (EBSCO)",
            "ACS eBooks",
            "ACS Journals",
            "AIP Publishing: Journal of Applied Physics",
            "AIP Publishing: Journal of Chemical Physics",
            "AIP Publishing: Physics of Fluids",
            "AIP Publishing: The Journal of Rheology",
            "Anopress",
            "ASPI",
            "Beck-Online",
            "BIOSIS Citation Index (Web of Science)",
            "Bloomsbury Applied Visual Arts",
            "Bookport",
            "Coronavirus Research Database",
            "ČSN online",
            "Current Contents Connect (Web of Science)",
            "Data Citation Index (Web of Science)",
            "De Gruyter eBooks and eJournals",
            "Derwent Innovations Index (Web of Science)",
            "eBook Collection (EBSCO)",
            "eBooks Open Access Monograph Collection (EBSCO)",
            "EBSCO",
            "Emerald (Management eJournals)",
            "Emerald Journals & Books",
            "EnviroNetBase",
            "FOODnetBASE",
            "IEEE Xplore",
            "IGI Global",
            "IOPscience",
            "Journal Citation Reports (JCR)",
            "Knovel",
            "Lecture Notes in Mathematics",
            "Library, Information Science & Technology Abstracts (EBSCO)",
            "MEDLINE",
            "MIT Press eBooks",
            "Nursing Reference Center Plus (EBSCO)",
            "Oxford Journals HSS Collection",
            "Oxford Scholarship Online (Linguistics)",
            "Oxford Scholarship Online (Psychology)",
            "Peter Lang eBooks",
            "ProQuest Central",
            "Reaxys",
            "RSC Journals",
            "SAGE Premier",
            "ScienceDirect",
            "SciFinder-n Scholar (Chemical Abstracts)",
            "Scopus",
            "SpringerLink",
            "Statista",
            "Taylor & Francis eBooks",
            "Taylor & Francis Online (Science & Technology Library)",
            "Teacher Reference Center (EBSCO)",
            "Vogue Archive",
            "Web of Science",
            "Wiley Online Library",
            "Zoological Record (Web of Science)"]
