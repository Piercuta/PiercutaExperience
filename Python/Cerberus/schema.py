{
    'cust_name': {
        'required': True,
        'type': 'string',
        'check_with': 'myTestFunc'
    },
    # 'cust_mail': {
    #     'type': 'string'
    # },
    # 'host_profile': {
    #     'type': 'string'
    # },
    'execute_days_off': {
        'type': 'boolean'
    },
    'execute_week_end': {
        'type': 'boolean'
    },
    'deploy': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema':{
                'name': {
                    'required': True,
                    'type': 'string'
                },
                'git_repo': {
                    'required': True,
                    'type': 'string'
                },
                'branch_name': {
                    'type': 'string'
                },
                'asg_suffix_type_linked': {
                    'type': 'string'
                },
                'build_env': {
                    'type': 'string'
                }
            }
        }
    },
    'bdd': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'type_bdd': {
                    'type': 'string'
                },
                'instance_type': {
                    'required': True,
                    'type': 'string',
                    'allowed': ['db.m3.2xlarge','db.m3.large','db.m3.medium','db.m3.xlarge','db.m4.2xlarge','db.m4.4xlarge','db.m4.10xlarge','db.m4.16xlarge','db.m4.large','db.m4.xlarge','db.m5.2xlarge','db.m5.4xlarge','db.m5.12xlarge','db.m5.24xlarge','db.m5.large','db.m5.xlarge','db.r3.2xlarge','db.r3.4xlarge','db.r3.8xlarge','db.r3.large','db.r3.xlarge','db.r4.2xlarge','db.r4.4xlarge','db.r4.8xlarge','db.r4.16xlarge','db.r4.large','db.r4.xlarge','db.r5.2xlarge','db.r5.4xlarge','db.r5.12xlarge','db.r5.24xlarge','db.r5.large','db.r5.xlarge','db.t2.2xlarge','db.t2.large','db.t2.medium','db.t2.micro','db.t2.small','db.t2.xlarge','db.t3.2xlarge','db.t3.large','db.t3.medium','db.t3.micro','db.t3.small','db.t3.xlarge']
                },
                'option_group': {
                    'required': True,
                    'type': 'string'
                },
                'parameter_group': {
                    'required': True,
                    'type': 'string'
                },
                'engine_type': {
                    'required': True,
                    'type': 'string'
                },
                'engine_version': {
                    'required': True,
                    'type': 'string'
                },
                'alloc_storage': {
                    'required': True,
                    'type': 'integer'
                },
                'name_source': {
                    'type': 'string'
                },
                'db_id': {
                    'type': 'string'
                },
                'connect_user': {
                    'type': 'string'
                },
                'connect_password': {
                    'type': 'string'
                },
                'connect_host_ext': {
                    'type': 'string'
                },
                'new_user': {
                    'type': 'string'
                },
                'new_user_pswd': {
                    'type': 'string'
                },
                'script_to_apply': {
                    'type': 'string'
                }
            }
        }
    },
    'elb_certificates': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'elb_certificate_arn': {
                    'type': 'string'
                }
            }
        }
    },
    'DefaultCidrBlock': {
        'type': 'string'
    },
    'SubnetBlocksCIDR': {
        'type': 'string'
    },
    'SecurityGroupIngressAllCIDR': {
        'type': 'string'
    },
    'PremGroupIngressIP': {
        'type': 'string'
    },
    'PremGroupIngressIP2': {
        'type': 'string'
    },
    'CustomerGroupIngressIP': {
        'type': 'string'
    },
    'CustomerGroupIngressIP2': {
        'type': 'string'
    },
    'OperatorEmail': {
        'type': 'string'
    },
    # 'SourcesIPForASGAccess': {
    #     'type': 'string'
    # },
    # 'SourcesIPForDBAccess': {
    #     'type': 'string'
    # },
    'AlarmThreshold': {
        'type': 'integer'
    },
    'elasticache_enabled': {
        'type': 'boolean'
    },
    'elasticache_engine': {
        'type': 'string'
    },
    'elasticache_engine_version': {
        'type': 'string'
    },
    'elasticache_instance_type': {
        'type': 'string'
    },
    'elasticache_number_of_node': {
        'type': 'integer'
    },
    'buckets': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema':{
                'name': {
                    'type': 'string'
                },
                'versioning_enabled': {
                    'type': 'boolean'
                },
                'policy_file': {
                    'type': 'string'
                }
            }
        }
    },
    'asg_groups': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema':{
                'ec2_keyname': {
                    'type': 'string'
                },
                'ec2_ami': {
                    'type': 'string'
                },
                'ec2_type': {
                    'type': 'string'
                },
                'ec2_suffix_type': {
                    'type': 'string'
                },
                'ec2_script': {
                    'type': 'string'
                },
                'ec2_volume_size': {
                    'type': 'integer'
                },
                'ec2_desired_capacity': {
                    'type': 'integer'
                },
                'ec2_health_check_path': {
                    'type': 'string'
                },
                'ec2_elb_listener_instance_port': {
                    'type': 'integer'
                },
                'ec2_elb_listener_load_balancer_port_1': {
                    'type': 'integer'
                },
                'ec2_elb_listener_load_balancer_port_2': {
                    'type': 'integer'
                },
                'ec2_elb_listener_load_balancer_port_3': {
                    'type': 'integer'
                },
                'ec2_elb_redirect_https': {
                    'type': 'boolean'
                },
                # 'ec2_elb_idle_timeout': {
                #     'type': 'integer'
                # },
                'dns_records': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                }
            }
        }
    },
    'user_pools': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema':{
                'UserPoolName': {
                    'required': True,
                    'type': 'string'
                },
                'UserPoolSource': {
                    'type': 'string'
                },
                'UserPoolClientName': {
                    'required': True,
                    'type': 'string'
                },
                'Policies':{
                    'type': 'dict',
                    'schema': {
                        'PasswordPolicy':{
                            'type':'dict',
                            'schema': {
                                'MinimumLength': {
                                    'type': 'integer',
                                },
                                'RequireUppercase': {
                                    'type': 'boolean'
                                },
                                'RequireLowercase': {
                                    'type': 'boolean'
                                },
                                'RequireNumbers': {
                                    'type': 'boolean'
                                },
                                'RequireSymbols': {
                                    'type': 'boolean'
                                },
                                'TemporaryPasswordValidityDays': {
                                    'type': 'integer'
                                }
                            }
                        }
                    }
                    
                },
                'Schema':{
                    'type': 'list',
                    'schema': {
                        'type':'dict',
                        'schema': {
                            'Name' :{
                                'type': 'string'
                            },
                            'AttributeDataType': {
                                'type': 'string'
                            },
                            'DeveloperOnlyAttribute': {
                                'type': 'boolean'
                            },
                            'Mutable': {
                                'type': 'boolean'
                            },
                            'Required': {
                                'type': 'boolean'
                            },
                            'StringAttributeConstraints': {
                                'type': 'dict',
                                'schema': {
                                    'MinLength': {
                                        'type': 'integer'
                                    },
                                    'MaxLength' : {
                                        'type': 'integer'
                                    }
                                }
                            },
                            'NumberAttributeConstraints': {
                                'type': 'dict',
                                'schema': {
                                    'MinValue': {
                                        'type': 'integer'
                                    },
                                    'MaxValue' : {
                                        'type': 'integer'
                                    }
                                }
                            }
                        }
                    }
                },
                'UsernameAttributes': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                },
                'AutoVerifiedAttributes': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                },
                'IdentityPoolName': {
                    'type': 'string' 
                },
                'AllowUnauthenticatedIdentities': {
                    'type': 'string'
                },
                'CognitoAuthenticatedPolicyStamemnt': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'Effect': {
                                'type': 'string'
                            },
                            'Action': {
                                'type': 'list',
                                'schema': {
                                    'type': 'string'
                                }
                            },
                            'Resource': {
                                'type': 'string'
                            }

                        }
                    }
                },
                'CognitoUnauthenticatedPolicyStatement': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'Effect': {
                                'type': 'string'
                            },
                            'Action': {
                                'type': 'list',
                                'schema': {
                                    'type': 'string'
                                }
                            },
                            'Resource': {
                                'type': 'string'
                            }

                        }
                    }
                },
                'MfaConfiguration': {
                    'type': 'string'
                },
                'GenerateSecret': {
                    'type': 'boolean'
                }
            }
        }
    },
    'dynamodb': {
        'type': 'dict',
        'schema': {
            'prefix_to_copy': {
                'type': 'string'
            },
            'tables': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        'name_source': {
                            'required': True,
                            'type': 'string'
                        },
                        'name_target': {
                            'type': 'string'
                        }
                    }
                }
            }
        }
    }
}