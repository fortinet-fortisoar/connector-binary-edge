## About the connector
Binaryedge helps to automatically scan the entire public internet, create real-time threat intelligence feeds or security reports that show the exposure of what is connected to the internet.
<p>This document provides information about the BinaryEdge Connector, which facilitates automated interactions, with a BinaryEdge server using FortiSOAR&trade; playbooks. Add the BinaryEdge Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with BinaryEdge.</p>
### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-binaryedge</pre>

## Prerequisites to configuring the connector
- You must have the credentials of BinaryEdge server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the BinaryEdge server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>BinaryEdge</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the binaryedge server to connect and perform automated operations.
</td>
</tr><tr><td>API key</td><td>Specify the API key to access the endpoint to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Host Details</td><td>Retrieves the recent events for the specified host, including details of exposed ports and services.</td><td>get_host_details <br/>Investigation</td></tr>
<tr><td>Get IP Risk Score Details</td><td>Retrieves a report from BinaryEdge for the IP address submitted. Scoring is based on all information found on BinaryEdge databases regarding an IP and refers to the level of exposure of a target, i.e, the higher the score, the greater the risk of exposure.</td><td>get_ip_risk_score_details <br/>Investigation</td></tr>
<tr><td>Get CVEs List</td><td>Retrieves list of CVEs that might affect a specific IP.</td><td>get_cves_list <br/>Investigation</td></tr>
<tr><td>Get Subdomain Details</td><td>Return list of subdomains known from the target domains.</td><td>get_subdomain_details <br/>Investigation</td></tr>
<tr><td>Get DNS Details</td><td>Return list of known DNS results for the target domain.</td><td>get_dns_details <br/>Investigation</td></tr>
</tbody></table>
### operation: Get Host Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the ip address whose details you want to retrieve from BinaryEdge.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "total": "",
        "query": "",
        "events": [
            {
                "results": [
                    {
                        "origin": {
                            "module": "",
                            "port": "",
                            "ip": "",
                            "type": "",
                            "ts": "",
                            "country": ""
                        },
                        "result": {
                            "data": {
                                "state": {
                                    "state": ""
                                },
                                "service": {
                                    "banner": " ",
                                    "method": "",
                                    "cpe": [
                                        ""
                                    ],
                                    "name": "",
                                    "product": ""
                                }
                            }
                        },
                        "target": {
                            "protocol": "",
                            "port": "",
                            "ip": ""
                        }
                    }
                ],
                "port": ""
            },
            {
                "results": [
                    {
                        "origin": {
                            "module": "",
                            "port": "",
                            "ip": "",
                            "type": "",
                            "ts": "",
                            "country": ""
                        },
                        "result": {
                            "data": {
                                "state": {
                                    "state": ""
                                },
                                "service": {
                                    "banner": "",
                                    "method": "",
                                    "cpe": [
                                        ""
                                    ],
                                    "name": "",
                                    "product": ""
                                }
                            }
                        },
                        "target": {
                            "protocol": "",
                            "port": "",
                            "ip": ""
                        }
                    }
                ],
                "port": ""
            }
        ]
    }
]</pre>
### operation: Get IP Risk Score Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the ip address whose risk score you want to retrieve from BinaryEdge.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "normalized_ip_score": "",
        "normalized_ip_score_detailed": {
            "cve": "",
            "attack_surface": "",
            "encryption": "",
            "rms": "",
            "storage": "",
            "web": "",
            "torrents": ""
        },
        "ip_score_detailed": {
            "cve": "",
            "attack_surface": "",
            "encryption": "",
            "rms": "",
            "storage": "",
            "web": "",
            "torrents": ""
        },
        "results_detailed": {
            "ports": {
                "open": [],
                "score": ""
            },
            "cve": {
                "result": [
                    {
                        "port": "",
                        "cve": [
                            {
                                "cpe": "",
                                "cve_list": [
                                    {
                                        "cve": "",
                                        "cvss": ""
                                    }
                                ],
                                "score": ""
                            }
                        ],
                        "score": ""
                    }
                ],
                "score": ""
            },
            "ssh": {
                "result": [
                    {
                        "port": "",
                        "algorithms": {
                            "mac": [
                                {
                                    "mac": "",
                                    "score": ""
                                },
                                {
                                    "mac": "",
                                    "score": ""
                                },
                                {
                                    "mac": "",
                                    "score": ""
                                }
                            ],
                            "key_exchange": [
                                {
                                    "kex": "",
                                    "score": ""
                                }
                            ],
                            "encryption": [
                                {
                                    "enc": "",
                                    "score": ""
                                }
                            ]
                        },
                        "keys": [
                            {
                                "fingerprint": "",
                                "key_length": {
                                    "length": "",
                                    "score": ""
                                },
                                "debian_key": {
                                    "found": "",
                                    "score": ""
                                }
                            }
                        ],
                        "score": ""
                    }
                ],
                "score": ""
            },
            "rms": {
                "result": [
                    {
                        "port": "",
                        "rms": "",
                        "score": ""
                    }
                ],
                "score": ""
            },
            "ssl": {
                "result": [
                    {
                        "port": "",
                        "heartbleed": {
                            "heartbleed": "",
                            "score": ""
                        },
                        "ccs": {
                            "ccs": "",
                            "score": ""
                        },
                        "crime": {
                            "crime": "",
                            "score": ""
                        },
                        "renegotiation": {
                            "renegotiation": "",
                            "score": ""
                        },
                        "ocsp": {
                            "ocsp": "",
                            "score": ""
                        },
                        "no_certificates": {
                            "no_certificates": "",
                            "score": ""
                        },
                        "leaf_certificate": {
                            "sha1_fingerprint": "",
                            "issuer": "",
                            "subject": "",
                            "validity": {
                                "date": "",
                                "status": "",
                                "score": ""
                            },
                            "signature": {
                                "signature": "",
                                "score": ""
                            },
                            "self_signed": {
                                "self_signed": "",
                                "score": ""
                            }
                        },
                        "other_certificates": [],
                        "ciphers": [
                            {
                                "drown": "",
                                "score": ""
                            },
                            {
                                "poodle": "",
                                "score": ""
                            },
                            {
                                "logjam": "",
                                "score": ""
                            }
                        ],
                        "score": ""
                    }
                ],
                "score": ""
            },
            "wec": {
                "result": [
                    {
                        "port": "",
                        "service": "",
                        "score": ""
                    }
                ],
                "score": ""
            },
            "ftp": {
                "result": [
                    {
                        "port": "",
                        "service": "",
                        "score": ""
                    }
                ],
                "score": ""
            },
            "http": {
                "result": [
                    {
                        "port": "",
                        "service": "",
                        "score": ""
                    }
                ],
                "score": ""
            },
            "storage": {
                "result": [
                    {
                        "port": "",
                        "product": "",
                        "score": ""
                    }
                ],
                "score": ""
            },
            "web": {
                "result": [
                    {
                        "port": "",
                        "headers": "",
                        "score": ""
                    }
                ],
                "score": ""
            },
            "torrents": {
                "result": [
                    {
                        "torrents": "",
                        "score": ""
                    }
                ],
                "score": ""
            }
        },
        "ip_address": ""
    }
]</pre>
### operation: Get CVEs List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>IP Address</td><td>Specify the ip address to retrieve the list of CVEs that might affect it.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "query": "",
        "events": {
            "ip": "",
            "ports": [],
            "results": [
                {
                    "port": "",
                    "cpe": [],
                    "ts": "",
                    "cves": []
                }
            ]
        }
    }
]</pre>
### operation: Get Subdomain Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Specify the domain whose subdomains you want to retrieve from BinaryEdge.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "query": "",
        "page": "",
        "pagesize": "",
        "total": "",
        "events": []
    }
]</pre>
### operation: Get DNS Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Specify the domain whose DNS details you want to retrieve from BinaryEdge.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "query": "",
        "page": "",
        "pagesize": "",
        "total": "",
        "events": [
            {
                "A": [],
                "updated_at": "",
                "domain": "",
                "root": ""
            },
            {
                "A": [],
                "MX": [],
                "NS": [],
                "updated_at": "",
                "domain": "",
                "root": ""
            },
            {
                "A": [],
                "updated_at": "",
                "domain": "",
                "root": ""
            },
            {
                "A": [],
                "updated_at": "",
                "domain": "",
                "root": ""
            }
        ]
    }
]</pre>
## Included playbooks
The `Sample - binaryedge - 1.0.0` playbook collection comes bundled with the BinaryEdge connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the BinaryEdge connector.

- Get CVEs List
- Get DNS Details
- Get Host Details
- Get IP Risk Score Details
- Get Subdomain Details

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
