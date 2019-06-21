#!/usr/bin/env python3
"""
experiences with cerberus
documentation at http://docs.python-cerberus.org/en/stable/usage.html#basic-usage
"""
from cerberus import Validator
import yaml

#in schema you can retrieve value by aws cli command 
#exemple for rds :
# aws rds describe-orderable-db-instance-options --profile prem-bam --engine oracle-ee --engine-version 12.1.0.2.v8 --license-model bring-your-own-license --query OrderableDBInstanceOptions[*].DBInstanceClass --output text | sed -e 'y/\t/\n/' | uniq > file.txt^C
# aws rds describe-orderable-db-instance-options --profile prem-bam --engine mariadb --query OrderableDBInstanceOptions[*].DBInstanceClass --output text | sed -e 'y/\t/\n/' | uniq > file.txt
class MyValidator(Validator):
    def _check_with_myTestFunc(self,field,value):
        if value == 'caca':
            self._error(field, "can't be caca")

schema = eval(open('schema.py','r').read())
v = MyValidator(schema, allow_unknown=False)
#v.require_all=True
#to allow unknown field
#v.allow_unknown = True
#add validate schema for unknown field
#v.allow_unknown = {'type' : 'string'}
with open('test.yaml', 'r') as stream:
            conf = yaml.load(stream)

#print(type(conf['user_pools'][0]['Policies']['PasswordPolicy']['MinimumLength']))
#print(conf['user_pools'][0]['Policies']['PasswordPolicy']['MinimumLength'])
print(v.validate(conf))

print(v.errors)