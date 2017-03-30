#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" script for generate process template directories

This is xxx
"""

import sys
import os
import argparse
import zipfile


def make_directories(path='.'):
    """ Generate template directories under target path"""

    top_process = [
        'SystemEngineering',
        'SafetyEngineering',
        'SoftwareEngineering',
        'Support',
        'Others'
    ]
    sub_process = [
        # SystemEngineering
        [
            'RequirementsDefinition',
            'ArchitecturalDesign',
            'IntegrationTesting',
            'Testing'
        ],
        # SafetyEngineering
        [
            'RequirementsDefinition',
            'Testing'
        ],
        # SoftwareEngineering
        [
            'RequirementsDefinition',
            'ArchitecturalDesign',
            'DetailedDesign',
            'Implementation',
            'UnitTesting',
            'IntegrationTesting',
            'ComprehensiveTesting'
        ],
        # Support
        [
            'ProjectManagement',
            'QualityAssurance',
            'RiskManagement',
            'DocumentationManagement',
            'ConfigurationManagement',
            'ProblemResolutionManagement',
            'ChangeManagement',
            'JointReview',
            'SubContructorManagement',
            'PreparationDevelopEnvironment'
        ],
        # Others
        [
            'dummy'
        ]
    ]

    for i, pt in enumerate(top_process):
        top_path = path + '/' + str(i) + '0_' + str(pt)
        for j, ps in enumerate(sub_process[i]):
            full_path = top_path + '/' + str(i) + str('%x' % (j + 1)) + '_' + ps
            os.makedirs(full_path)


def fild_all_files(path):
    """ find all directories & files under target path """
    for root, dirs, files in os.walk(path):
        yield root
        for f in files:
            yield os.path.join(root, f)


def main(args):
    """ Main routine """
    parser = argparse.ArgumentParser(description='This is command for generating development process template directories')
    parser.add_argument('path', help='target top path of generated directories')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    if args.path:
        make_directories(args.path)

        z = zipfile.ZipFile('process_template.zip', 'w', zipfile.ZIP_DEFLATED)

        for f in fild_all_files(args.path):
            print f
            z.write(f)

        z.close()

    else:
        print("Argument error. Please input path!")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
