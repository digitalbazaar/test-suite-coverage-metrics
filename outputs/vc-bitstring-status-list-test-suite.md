# Test Suite Coverage Metrics
## vc-bitstring-status-list-test-suite

### Summary of supported features and implementations

*This highlights features that have less than 2 passing implementations.*
Risk Score: Critical
Failed %: 65
Failed Count: 15
Total Count: 23

#### Details
*Features with a state of pending are not considered at risk.*

##### At Risk Features

- Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0].
- If present, the id value is expected to be a URL that identifies the status information associated with the verifiable credential. It MUST NOT be the URL for the status list.
- The type property MUST be BitstringStatusListEntry.
- The purpose of the status entry MUST be a string.
- The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10.
- The statusListCredential property MUST be a URL to a verifiable credential.
- When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value.
- When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0].
- The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value.
- The type of the credential subject, which is the status list, MUST be BitstringStatusList.
- The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings.
- The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values.
- The uncompressed bitstring MUST be at least 16KB in size.
- ACA-py
- Digital Bazaar

##### Pending Features

- If present, statusSize MUST be an integer greater than zero.
- If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present.
- The number of status messages MUST equal the number of possible values.
- If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize.
- statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1.
- If the statusMessage array is present, each element MUST contain the two properties "status" and "message".
- If present, the "statusReference" value MUST be a URL or an array of URLs [URL] which dereference(s) to material related to the status.
- The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring.

### Summary of normative statements coverage

| Count (Suite) | Count (Spec) | Matches | Unmatched (Suite) | Unmatched (Spec) |
| ------- | ------- | ------- | ------- | ------- |
| 21 | 39 | 18 |  3 |  21 |

### Details
#### Test Suite Statements
```json
[
  "Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0].",
  "If present, the id value is expected to be a URL that identifies the status information associated with the verifiable credential. It MUST NOT be the URL for the status list.",
  "The type property MUST be BitstringStatusListEntry. ",
  "The purpose of the status entry MUST be a string.",
  "The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10.",
  "The statusListCredential property MUST be a URL to a verifiable credential.",
  "When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value.",
  "If present, statusSize MUST be an integer greater than zero.",
  "If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present.",
  "The number of status messages MUST equal the number of possible values.",
  "If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize.",
  "statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1.",
  "If the statusMessage array is present, each element MUST contain the two properties \"status\" and \"message\".",
  "If present, the \"statusReference\" value MUST be a URL or an array of URLs [URL] which dereference(s) to material related to the status.",
  "When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0].",
  "The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value.",
  "The type of the credential subject, which is the status list, MUST be BitstringStatusList.",
  "The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings.",
  "The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values.",
  "The uncompressed bitstring MUST be at least 16KB in size.",
  "The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring."
]
```
#### Specifications Statements
```json
[
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0].",
  "It MUST NOT be the URL for the status list",
  "The type property MUST be BitstringStatusListEntry.",
  "The purpose of the status entry MUST be a string",
  "While the value of the string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential",
  "The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10",
  "The statusListCredential property MUST be a URL to a verifiable credential",
  "When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value.",
  "If statusSize is not present as a property of the credentialStatus, then statusSize MUST be processed as 1",
  "If present, statusSize MUST be an integer greater than zero",
  "If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present, and the number of status messages MUST equal the number of possible values.",
  "If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize (e.g., statusMessage array MUST have 2 elements if statusSize has 1 bit, 4 elements if statusSize has 2 bits, 8 elements if statusSize has 3 bits, etc.)",
  "statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1",
  "If the statusMessage array is present, each element MUST contain the two properties described below, and MAY contain additional properties",
  "If present, its value MUST be a URL or an array of URLs [URL] which dereference to material related to the status",
  "When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0], that expresses the data model in this section",
  "One way to resolve this conflict is to remove ttl and specify that caching behavior can be expressed using protocol mechanisms (such as the expires header in HTTP), and that any caching performed MUST align with the validUntil value for the verifiable credential",
  "The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value.",
  "The type of the credential subject, which is the status list, MUST be BitstringStatusList.",
  "The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings",
  "While the value of each string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential",
  "The status message descriptions MUST be defined in credentialSubject.statusMessages",
  "credentialSubject.statusSize MUST be specified when this statusPurpose value is used.",
  "The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values",
  "The uncompressed bitstring MUST be at least 16KB in size",
  "The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring",
  "If not present, implementers MUST use a value of 300000 for this property",
  "A verifier MUST NOT use a cached BitstringStatusListCredential that was cached for more than the ttl duration prior to the start of verification operation on a verifiable credential",
  "Data Model whose value is malformed due to not complying with associated 'MUST' statements, a MALFORMED_VALUE_ERROR MUST be raised.",
  "The following process, or one generating the exact output, MUST be followed when producing a BitstringStatusListCredential",
  "The following process, or one generating the exact output, MUST be followed when validating a verifiable credential that is contained in a BitstringStatusListCredential",
  "If the credentialIndex multiplied by the size is a value outside of the range of the bitstring, a RANGE_ERROR MUST be raised.",
  "If such a feature is supported, and if query parameters are supported by the URL scheme, then the name of the query parameter MUST be timestamp and the value MUST be a valid URL-encoded [XMLSCHEMA11-2] dateTimeStamp string value",
  "The result of dereferencing such a timestamp-parameterized URL MUST be either a status list credential containing the status list as it existed at the given point in time, or a STATUS_RETRIEVAL_ERROR",
  "The following process, or one generating the exact output, MUST be followed when generating a status list bitstring",
  "The following process, or one generating the exact output, MUST be followed when expanding a compressed status list bitstring",
  "The type value of the error object MUST be a URL that starts with the value https://www.w3.org/ns/credentials/status-list# and ends with the value in the section listed below.",
  "The code value MUST be the integer code described in the table below (in parentheses, beside the type name)."
]
```
#### Matched Statements
```json
[
  [
    "Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0].",
    "Any expression of the data model in this section MUST be expressed in a conforming verifiable credential as defined in [VC-DATA-MODEL-2.0]."
  ],
  [
    "The type property MUST be BitstringStatusListEntry.",
    "The type property MUST be BitstringStatusListEntry. "
  ],
  [
    "The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10",
    "The statusListIndex property MUST be an arbitrary size integer greater than or equal to 0, expressed as a string in base 10."
  ],
  [
    "When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value.",
    "When the URL is dereferenced, the resulting verifiable credential MUST have type property that includes the BitstringStatusListCredential value."
  ],
  [
    "If present, statusSize MUST be an integer greater than zero",
    "If present, statusSize MUST be an integer greater than zero."
  ],
  [
    "statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1",
    "statusMessage MAY be present if statusSize is 1, and MUST be present if statusSize is greater than 1."
  ],
  [
    "If present, its value MUST be a URL or an array of URLs [URL] which dereference to material related to the status",
    "If present, the \"statusReference\" value MUST be a URL or an array of URLs [URL] which dereference(s) to material related to the status."
  ],
  [
    "The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value.",
    "The verifiable credential that contains the status list MUST express a type property that includes the BitstringStatusListCredential value."
  ],
  [
    "The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings",
    "The value of the purpose property of the status entry, statusPurpose, MUST be one or more strings."
  ],
  [
    "The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values",
    "The encodedList property of the credential subject MUST be a Multibase-encoded base64url (with no padding) [RFC4648] representation of the GZIP-compressed [RFC1952] bitstring values for the associated range of verifiable credential status values."
  ],
  [
    "The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring",
    "The bitstring MUST be encoded such that the first index, with a value of zero (0), is located at the left-most bit in the bitstring and the last index, with a value of one less than the length of the bitstring (bitstring_length - 1), is located at the right-most bit in the bitstring."
  ],
  [
    "The purpose of the status entry MUST be a string",
    "The purpose of the status entry MUST be a string."
  ],
  [
    "The statusListCredential property MUST be a URL to a verifiable credential",
    "The statusListCredential property MUST be a URL to a verifiable credential."
  ],
  [
    "If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present, and the number of status messages MUST equal the number of possible values.",
    "If statusSize is provided and is greater than 1, then the property credentialStatus.statusMessage MUST be present."
  ],
  [
    "If the statusMessage array is present, each element MUST contain the two properties described below, and MAY contain additional properties",
    "If the statusMessage array is present, each element MUST contain the two properties \"status\" and \"message\"."
  ],
  [
    "The type of the credential subject, which is the status list, MUST be BitstringStatusList.",
    "The type of the credential subject, which is the status list, MUST be BitstringStatusList."
  ],
  [
    "The uncompressed bitstring MUST be at least 16KB in size",
    "The uncompressed bitstring MUST be at least 16KB in size."
  ],
  [
    "When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0], that expresses the data model in this section",
    "When a status list verifiable credential is published, it MUST be a conforming document, as defined in [VC-DATA-MODEL-2.0]."
  ]
]
```
#### Unmatched Test Suite Statements
```json
[
  "If present, the id value is expected to be a URL that identifies the status information associated with the verifiable credential. It MUST NOT be the URL for the status list.",
  "The number of status messages MUST equal the number of possible values.",
  "If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize."
]
```
#### Unmatched Specifications Statements
```json
[
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "It MUST NOT be the URL for the status list",
  "While the value of the string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential",
  "If statusSize is not present as a property of the credentialStatus, then statusSize MUST be processed as 1",
  "If present, the statusMessage property MUST be an array, the length of which MUST equal the number of possible status messages indicated by statusSize (e.g., statusMessage array MUST have 2 elements if statusSize has 1 bit, 4 elements if statusSize has 2 bits, 8 elements if statusSize has 3 bits, etc.)",
  "One way to resolve this conflict is to remove ttl and specify that caching behavior can be expressed using protocol mechanisms (such as the expires header in HTTP), and that any caching performed MUST align with the validUntil value for the verifiable credential",
  "While the value of each string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential",
  "The status message descriptions MUST be defined in credentialSubject.statusMessages",
  "credentialSubject.statusSize MUST be specified when this statusPurpose value is used.",
  "If not present, implementers MUST use a value of 300000 for this property",
  "A verifier MUST NOT use a cached BitstringStatusListCredential that was cached for more than the ttl duration prior to the start of verification operation on a verifiable credential",
  "Data Model whose value is malformed due to not complying with associated 'MUST' statements, a MALFORMED_VALUE_ERROR MUST be raised.",
  "The following process, or one generating the exact output, MUST be followed when producing a BitstringStatusListCredential",
  "The following process, or one generating the exact output, MUST be followed when validating a verifiable credential that is contained in a BitstringStatusListCredential",
  "If the credentialIndex multiplied by the size is a value outside of the range of the bitstring, a RANGE_ERROR MUST be raised.",
  "If such a feature is supported, and if query parameters are supported by the URL scheme, then the name of the query parameter MUST be timestamp and the value MUST be a valid URL-encoded [XMLSCHEMA11-2] dateTimeStamp string value",
  "The result of dereferencing such a timestamp-parameterized URL MUST be either a status list credential containing the status list as it existed at the given point in time, or a STATUS_RETRIEVAL_ERROR",
  "The following process, or one generating the exact output, MUST be followed when generating a status list bitstring",
  "The following process, or one generating the exact output, MUST be followed when expanding a compressed status list bitstring",
  "The type value of the error object MUST be a URL that starts with the value https://www.w3.org/ns/credentials/status-list# and ends with the value in the section listed below.",
  "The code value MUST be the integer code described in the table below (in parentheses, beside the type name)."
]
```