---
description: >-
  Following are the use-case specifications required by the organisation IT
  administrators for updating Data Policies required for an identified Consent
  Agreements (within postpartum and infant care)
---

# UC-C-PIC-A: Organisation Administration Use Cases (CONFIGURATION)

## **Table of Contents**

[UC-C-PIC-A-001:\
Postpartum and infant care (Configuration CREATE)](uc-c-pic-a-organisation-administration-use-cases-configuration.md#uc-c-pic-a-001-postpartum-and-infant-care-configuration-create)

[UC-C-PIC-A-002:\
Postpartum and infant care (Configuration UPDATE)](uc-c-pic-a-organisation-administration-use-cases-configuration.md#uc-c-pic-a-002-postpartum-and-infant-care-configuration-update)

[UC-C-PIC-A-003:\
Postpartum and infant care (Configuration READ)](uc-c-pic-a-organisation-administration-use-cases-configuration.md#uc-c-pic-a-003-postpartum-and-infant-care-configuration-read)

[UC-C-PIC-A-004:\
Postpartum and infant care (Configuration DELETE)](uc-c-pic-a-organisation-administration-use-cases-configuration.md#uc-c-pic-a-004-postpartum-and-infant-care-configuration-delete)

[UC-C-PIC-A-005:\
Postpartum and infant care (Configuration NOTIFICATIONS)](uc-c-pic-a-organisation-administration-use-cases-configuration.md#uc-c-pic-a-005-postpartum-and-infant-care-configuration-notifications)&#x20;

##

UC-C-PIC-A-001:\
Postpartum and infant care (Configuration CREATE)
-------------------------------------------------

| **ID**                                                                                                                         | UC-C-PIC-001                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**                                                                                                                       | Postpartum and infant care (Configuration CREATE)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Description                                                                                                                    | The use case implements configuration of a consent agreement towards infant care use case scenarios. This results in a saved configuration to be issued to all mothers requiring infant care.                                                                                                                                                                                                                                                                                                                                                                                                    |
| <p>Trigger<br>(the event that triggers the use case)</p>                                                                       | <ol><li>The (healthcare) application admin/user wishes to configure the policies associated with the data usage.</li><li>Any change in the pre-condition that requires a re-configuration. </li></ol>                                                                                                                                                                                                                                                                                                                                                                                            |
| <p>Preconditions<br>(list of conditions that MUST be met in order for the use case to be successful)</p>                       | <ol><li>The  (healthcare) application admin/user is logged into the system and has sufficient privileges to use the system</li><li>A healthcare policy exists, and is based on existing data laws for healthcare. </li><li>Assumption: consent is needed for pulling data from another system of the mother needing care.</li></ol>                                                                                                                                                                                                                                                              |
| Data inputs                                                                                                                    | <ol><li>Existing data policies relevant to the healthcare scenario</li><li>Any legal information, standards.</li></ol>                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <p>Actors<br>(a person, a company or organisation, a computer program, or a computer system - hardware, software, or both)</p> | <ol><li>The  (healthcare) application admin/user configures the data usage policy. (a person, IT admin)</li><li>The health-care provider application. (a computer system)</li><li>DPO, Auditors (A person, or an independent authority)</li></ol><p><br></p><p>Optionally: a data intermediary or a data operator.</p>                                                                                                                                                                                                                                                                           |
| Normal Course (what happens if the event is triggered and the preconditions have been met)                                     | <ol><li>The healthcare application user is able to invoke the configuration workflow.</li><li>The healthcare user uses the existing policy relevant to registering for postpartum and infant care. This could be signed off by the organisation's DPO, for example. </li><li>The data required are:</li><li><p></p><ol><li>Usage purpose</li><li>Data policies and rules</li><li>Define what data is being collected</li></ol></li><li>The configuration is saved. </li><li>Once the DPO approves, the configuration is published towards the end-use case.  I.e. registration system.</li></ol> |
| <p>Alternative Course<br>(links to other use cases in case there are different ways how to solve the same use case)</p>        | <ol><li>Data configuration error scenarios</li><li>DPO disapproves and the configuration is re-submitted for review and approval. </li></ol>                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Data output                                                                                                                    | <ol><li>The consent configuration data</li></ol>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Post-Conditions (the success criteria)                                                                                         | <ol><li>The data usage policy is saved in the system and is available for the month to consent to during the registration process.</li><li>The system is now configured and ready for collecting user consent during a registration workflow.</li></ol>                                                                                                                                                                                                                                                                                                                                          |
| <p>Exceptions<br>(error situations)</p>                                                                                        | (TBD - Should align with other error scenarios.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <p>Related BBs<br>(working groups related to that particular use case)</p>                                                     | <ol><li>Identity BB (Required for acquiring authentication token)</li><li>Workflow BB - workflow management</li><li>Information Mediator BB - providing interfaces</li><li>Security BB - supervision</li></ol>                                                                                                                                                                                                                                                                                                                                                                                   |

### Sequence diagram

<figure><img src="https://lh6.googleusercontent.com/rx5FypRNN6urIidElfCeeklNDJPxcz8EbP2bSqslvf4HpChC1bnioz4c35y3Sj3XkEUsq-Saq8EkGeSPAqkSxtp1YzlueiC9ucuXcsG-huwR-0336tmht20D7Hq6I3njNZ1IiVeauWkW0waA87dBYg" alt=""><figcaption></figcaption></figure>

[Diagram source](https://www.websequencediagrams.com/files/render?link=uKuPezFhfn7wVAdr5Mbg6PwpZ6lr9uE7gmY7kzfnzhOMb7AyNnKv79pJZL3pq9aN)

\


The following sequence diagrams details the role of the Independent Authority and the DPIA (Data Protection Impact Assessment) as the document upon which the postpartum infant care program can rely to parametrise the healthcare application for interacting with the consent management BB.

<figure><img src="https://lh5.googleusercontent.com/AK1vJOZoljR2EfRr_z9ND9hGWvUlYwz_P_snucAPNUFIYClM30uF_tL_dkKxPTU7a4G-2vtQZ30bAq7uRGaxhpRncOdjiKbNtqrP3_USVi7IlCm97T0SoRT-Y8V-wTkIkjGp_5NqAw4araxvQgZehA" alt=""><figcaption></figcaption></figure>

[Diagram Source](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgVUMtQy1QSUMtMDAxOiBDcmVhdGUgbmV3IGFncmVtZW50CgpBY3RvciBIZWFsdGhjYXJlIGFwcGxpY2F0aW9uCgABFi0-Q29uc2VudCBNYW5hZwBEBSBCQjpjAFIOAFsGABYVLT5QUElDIFByb2dyYW06IGNoZWNrRFBJQQoADAwtPisAFBMgcmVxdWVzdCBsZWdpdGltYWN5Cm5vdGUgb3ZlciBJbmRlcGVuZGVudCBBdXRob3JpdHk6IERQTyxBdWRpdG9ycywgYQAzCXRlIGEAHgggaW4gdGhlIFBQTEMgcACBFQYganVyaXNkaWMAggoFAIEODwBVF2dldExhc3RBcHByb3ZlZACBUgUAgQIVLT4tAIF5DnJldHVybgAsEQCCBg4tAIJnFgAlGACCaRcrAC8XAIM-BkEAgzcIV2l0aExhc3QALxwtAIQnFjogTgCDfQwAUwdkIHN1Y2Nlc3NmdWxseQoKCg\&s=default)

\
\


UC-C-PIC-A-002:\
Postpartum and infant care (Configuration UPDATE)
-------------------------------------------------

| **ID**                                                                                                                                                           | UC-C-PIC-002                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                                                                                                                                                         | Postpartum and infant care (Configuration UPDATE)                                                                                                                                                                                                                                                                                   |
| **Description**                                                                                                                                                  | Here, an organisation Administrator updates Consent Agreement based on the Data Policy requirements..                                                                                                                                                                                                                               |
| <p><strong>Trigger</strong><br><strong>(the event that triggers the use case)</strong></p>                                                                       | <ol><li>The (healthcare) application admin/user wishes to configure the policies associated with the data usage.</li><li>Any change in the pre-condition that requires a re-configuration. </li></ol>                                                                                                                               |
| <p><strong>Preconditions</strong><br><strong>(list of conditions that MUST be met in order for the use case to be successful)</strong></p>                       | <ol><li>The  (healthcare) application admin/user is logged into the system and has sufficient privileges to use the system</li><li>A healthcare policy exists, and is based on existing data laws for healthcare. </li><li>Assumption: consent is needed for pulling data from another system of the mother needing care.</li></ol> |
| **Data inputs**                                                                                                                                                  | <ol><li>Existing data policies relevant to the healthcare scenario</li><li>Any legal information, standards.</li></ol>                                                                                                                                                                                                              |
| <p><strong>Actors</strong><br><strong>(a person, a company or organisation, a computer program, or a computer system - hardware, software, or both)</strong></p> | <ol><li>The  (healthcare) application admin/user configures the data usage policy. (a person, IT admin)</li><li>The health-care provider application. (a computer system)</li><li>DPO, Auditors (A person, or an independent authority)</li></ol><p><br></p><p>Optionally: a data intermediary or a data operator.</p>              |
| **Normal Course (what happens if the event is triggered and the preconditions have been met)**                                                                   | TBD                                                                                                                                                                                                                                                                                                                                 |
| <p><strong>Alternative Course</strong><br><strong>(links to other use cases in case there are different ways how to solve the same use case)</strong></p>        | <ol><li>Data configuration error scenarios</li><li>DPO disapproves and the configuration is re-submitted for review and approval. </li></ol>                                                                                                                                                                                        |
| **Data output**                                                                                                                                                  | <ol><li>Updated consent configuration data, Revision</li></ol>                                                                                                                                                                                                                                                                      |
| **Post-Conditions (the success criteria)**                                                                                                                       | <ol><li>The data usage policy is saved in the system and is available for the month to consent to during the registration process.</li><li>The system is now configured and ready for collecting user consent during a registration workflow.</li></ol>                                                                             |
| <p><strong>Exceptions</strong><br><strong>(error situations)</strong></p>                                                                                        | (TBD - Should align with other error scenarios.)                                                                                                                                                                                                                                                                                    |
| <p><strong>Related BBs</strong><br><strong>(working groups related to that particular use case)</strong></p>                                                     | <ol><li>Identity BB (Required for acquiring authentication token)</li><li>Workflow BB - workflow management</li><li>Registries BB - stores the data agreement data,</li><li>Information Mediator BB - providing interfaces</li><li>Security BB - supervision</li></ol>                                                              |

### Sequence diagram

<figure><img src="https://lh4.googleusercontent.com/WupcaLDRoa0kNg5SC_Yo5n4wV4L5VGnUReVrSuOSX2Qi225cYA01SryXe0w7UbF_aou4tDpNmW-adBTHEnXKxYirKCDiNq7AY1VskRAU_UCkTIW6Dvg7jm51wsjJRK8r4VF0tNMgrTE0Eb0C0NxaPw" alt=""><figcaption></figcaption></figure>

[Diagram source](https://www.websequencediagrams.com/?lz=dGl0bGUgVUMtQy1QSUMtMDAxOiBDb25zZW50IC0gUG9zdHBhcnR1bSBhbmQgaW5mYW50IGNhcmUgKENvbmZpZ3VyYXRpb24gVVBEQVRFKQoKCmFjdG9yIEFwcGxpYwAWBmFkbWluCgoAAhEtPitIZWFsdGgATAVhACgKOiBJbnZva2UgVXBkYXRlIEV4aXN0aW5nIEFncmVlbWVudAoKbm90ZSByaWdodCBvZgBcEyAgICBQcmVjb25kaXRpb25zOiBUaGUgRGF0YSBTb3VyY2UgAB8FYW5kAA8GVXNpbmcgU2VydmljZSBoYXMgYWdyZWVkACEGdG8gc2hhcmUgZGF0YS4AWQUAXgVOb3RlOiBUaGlzIHMANAdpcyBhbHJlYWR5IHByb3Zpc2lvbmVkAIEMBW91dHNpZGUgb2YgdGhlAIJgCU1hbmFnAIFTBSBCQgBSCwCBIRBwdXRzADQFcmVxdWlyACwGAFMGbiBhbnkAgTUUaW4AgTQFaW5nIHRoZWlyAIFwBmRhdGEsIHdoZXRoZXIgYSBjAINsB2lzIG5lZWRlZCBldGMAgVwLQWxsIGNob2ljZXMgZG9uZSBieQCBPQUAg1YFIACDOgUAgW0GAIJzBXZlcmlmaWVkIGJ5IGxlZ2FsIGFkdmlzb3J5CmVuZCBub3RlCgoAg2UWIC0tPisAggMVOiBDaGFuZ2VzIHRvAIN-CwCCLxUtPitSZWdpc3RyeQA1BVNhdmVzIGEgbmV3IHJlAIMNBgCEMw8AIw0AhF8JIFIAJwcgc2F2ZWQgcGVyc2lzdGVudGx5CgBYCy0tPi0AgR8XU3VjY2VzcwCBEhctPi0AhWwYUmVzdWx0c1xuKElEIG9mAIE4BQCFDgUAhCQFAIE\_CCxcbkV4cGlyZWQAgz0IKQCCRBctLT4tAIcGETogRGlzcGxheXMgcgBqBgCHFRMAhw4bQ2hvb3NlIGFjAIZfBSBmb3IgcHJldmlvdXMAhE0IAHUaAINRGACBQg8gLSBzAIQxB2lmAIhOB1xuAIILBwCFMggAhgwHZACCTxlXb3JrZmxvdwCERgVQcm9jZXNzIGUAWw9saXN0CgAfCy0tPgCEdhdqb2Igc3RhcnQAWBsAiUYYAIFQEGJlaW5nIHAAgQ4GZWQAgwE\_\&s=default&)



## UC-C-PIC-A-003: Postpartum and infant care (Configuration READ)



## UC-C-PIC-A-004: Postpartum and infant care (Configuration DELETE)



## UC-C-PIC-A-005: Postpartum and infant care (Configuration NOTIFICATIONS)