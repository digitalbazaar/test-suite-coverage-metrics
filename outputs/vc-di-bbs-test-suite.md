# Test Suite Coverage Metrics
## vc-di-bbs-test-suite

### Summary of supported features and implementations

*This highlights features that have less than 2 passing implementations.*
Risk Score: Low
Failed %: 2
Failed Count: 3
Total Count: 108

#### Details
*Features with a state of pending are not considered at risk.*

##### At Risk Features

- MUST verify with full array revealed properties
- MUST verify with fewer array revealed properties
- MUST verify w/o first element revealed properties

##### Pending Features


### Summary of normative statements coverage

| Count (Suite) | Count (Spec) | Matches | Unmatched (Suite) | Unmatched (Spec) |
| ------- | ------- | ------- | ------- | ------- |
| 73 | 79 | 32 |  41 |  47 |

### Details
#### Test Suite Statements
```json
[
  "When expressing a data integrity proof on an object, a proof property MUST be used.",
  "If present (proof), its value MUST be either a single object, or an unordered set of objects.",
  "(\"proof.id\") An optional identifier for the proof, which MUST be a URL.",
  "The specific type of proof MUST be specified as a string that maps to a URL.",
  "The type property MUST contain the string DataIntegrityProof.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.",
  "If specified (proof.cryptosuite), its value MUST be a string.",
  "A verification method is the means and information needed to verify the proof. If included, the value MUST be a string that maps to a [URL].",
  "The reason the proof was created (\"proof.proofPurpose\") MUST be specified as a string that maps to a URL.",
  "(\"proof.proofValue\") A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data.",
  "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "The cryptosuite property of the proof MUST be bbs-2023.",
  "The type property of the proof MUST be DataIntegrityProof.",
  "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3. Algorithms.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The verificationMethod property of the proof MUST be a URL.",
  "Dereferencing \"verificationMethod\" MUST result in an object containing a type property with \"Multikey\" value.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod).",
  "the HMAC key MUST be the same length as the digest size",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "Initialize components to an array that is the result of CBOR-decoding the bytes that follow the three-byte BBS disclosure proof header. If the result is not an array of five or six elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The cryptosuite property of the proof MUST be bbs-2023.",
  "The type property of the proof MUST be DataIntegrityProof.",
  "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3. Algorithms.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The verificationMethod property of the proof MUST be a URL.",
  "Dereferencing \"verificationMethod\" MUST result in an object containing a type property with \"Multikey\" value.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod).",
  "the HMAC key MUST be the same length as the digest size",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "Initialize components to an array that is the result of CBOR-decoding the bytes that follow the three-byte BBS disclosure proof header. If the result is not an array of five or six elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "(\"proof.proofValue\") A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "(\"proof.proofValue\") A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Whenever this algorithm (base proof) encodes strings, it MUST use UTF-8 encoding.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite). A proof configuration object is produced as output.",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Whenever this algorithm (base proof) encodes strings, it MUST use UTF-8 encoding.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite). A proof configuration object is produced as output.",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
]
```
#### Specifications Statements
```json
[
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "When expressing a data integrity proof on an object, a proof property MUST be used",
  "If present, its value MUST be either a single object, or an unordered set of objects, expressed using the properties below:",
  "An optional identifier for the proof, which MUST be a URL [URL], such as a UUID as a URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5)",
  "The specific type of proof MUST be specified as a string that maps to a URL [URL]",
  "The reason the proof was created MUST be specified as a string that maps to a URL [URL]",
  "If included, the value MUST be a string that maps to a [URL]",
  "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified",
  "If specified, its value MUST be a string.",
  "The date and time the proof was created is OPTIONAL and, if included, MUST be specified as an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC",
  "If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC",
  "If specified, the associated value MUST be either a string, or an unordered set of strings",
  "The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data",
  "If present, it MUST be a string value or an unordered list of string values",
  "Each value identifies another data integrity proof, all of which MUST also verify for the current proof to be considered verified",
  "If present, the digestMultibase value MUST be a single string value, or an list of string values, each of which is a Multibase-encoded Multihash value.",
  "Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below:",
  "Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.",
  "Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document",
  "Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.",
  "However, if an @context declaration is not included, extensions (such as the addition of new properties) related to this specification or corresponding cryptosuites MUST NOT be made.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "The specification MUST be published as a human-readable document at a URL.",
  "The specification MUST identify a cryptographic suite type and any parameters that can be used with the suite.",
  "The specification MUST detail the transformation algorithms (if any), parameters, and other necessary details, used to modify input data into the data to be protected.",
  "The specification MUST detail the hashing algorithms parameters, and other necessary details used to perform cryptographic hashing to the data to be protected.",
  "The specification MUST detail the proof serialization algorithms, parameters, and other necessary details used to perform cryptographic protection of the data.",
  "The specification MUST detail the proof verification algorithms, parameters, and other necessary details used to perform cryptographic verification of the data.",
  "The specification MUST define a data integrity cryptographic suite instantiation algorithm that accepts a set of options (map options) and returns a cryptosuite instance (struct cryptosuite)",
  "The specification MUST detail any known resource starvation attack that can occur in an algorithm and provide testable mitigations against each attack.",
  "The specification MUST contain a Security Considerations section detailing security considerations specific to the cryptographic suite.",
  "The specification MUST contain a Privacy Considerations section detailing privacy considerations specific to the cryptographic suite.",
  "The JSON-LD context associated with the cryptographic suite MUST have its terms protected from unsafe redefinition, by use of the @protected keyword.",
  "The type property MUST contain the string DataIntegrityProof.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite",
  "If the processing environment supports string subtypes, the subtype of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype.",
  "The proofValue property MUST be used, as specified in Section 2.1 Proofs.",
  "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
  "If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.",
  "If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "When a step says 'an error MUST be raised', it means that a verification result MUST be returned with a verified value of false and a non-empty errors list.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If domain was given, and it does not contain the same strings as proof.domain (treating a single string as a set containing just that string), an error MUST be raised and SHOULD convey an error type of INVALID_DOMAIN_ERROR.",
  "If challenge was given, and it does not match proof.challenge, an error MUST be raised and SHOULD convey an error type of INVALID_CHALLENGE_ERROR.",
  "If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.",
  "The code value MUST be the integer code described in the table below (in parentheses, beside the type name).",
  "Algorithms of this document MUST be enforced.",
  "Any other encodings MUST NOT be allowed.",
  "The verificationMethod property of the proof MUST be a URL",
  "Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Multikey.",
  "The type property of the proof MUST be DataIntegrityProof.",
  "The cryptosuite property of the proof MUST be bbs-2023.",
  "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components",
  "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the proofValue string does not start with u (U+0075, LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the result is not an array of five, six, or seven elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If featureOption is set to 'anonymous_holder_binding' or 'pseudonym_hidden_pid', the commitment_with_proof input MUST be supplied.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader",
  "Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If featureOption is set to 'anonymous_holder_binding' or 'pseudonym_hidden_pid', the commitment_with_proof input MUST be supplied; if not supplied, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR",
  "If featureOption equals 'anonymous_holder_binding', the REQUIRED additional inputs are holderSecret and proverBlind",
  "If featureOption equals 'pseudonym_issuer_pid', the REQUIRED additional input is the verifier_id which is communicated to the holder by the verifier",
  "If featureOption equals 'pseudonym_hidden_pid', the REQUIRED additional inputs are the pid, proverBlind (both known to holder), and verifier_id which is communicated to the holder by the verifier"
]
```
#### Matched Statements
```json
[
  [
    "Conforming processors MUST produce errors when non-conforming documents are consumed.",
    "Conforming processors MUST produce errors when non-conforming documents are consumed."
  ],
  [
    "If present, its value MUST be either a single object, or an unordered set of objects, expressed using the properties below:",
    "If present (proof), its value MUST be either a single object, or an unordered set of objects."
  ],
  [
    "The specific type of proof MUST be specified as a string that maps to a URL [URL]",
    "The specific type of proof MUST be specified as a string that maps to a URL."
  ],
  [
    "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified",
    "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified."
  ],
  [
    "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
    "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document."
  ],
  [
    "The type property MUST contain the string DataIntegrityProof.",
    "The type property MUST contain the string DataIntegrityProof."
  ],
  [
    "The proofValue property MUST be used, as specified in Section 2.1 Proofs.",
    "The proofValue property MUST be used, as specified in 2.1 Proofs."
  ],
  [
    "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
    "Whenever this algorithm (base proof) encodes strings, it MUST use UTF-8 encoding."
  ],
  [
    "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR."
  ],
  [
    "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
    "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
  ],
  [
    "If challenge was given, and it does not match proof.challenge, an error MUST be raised and SHOULD convey an error type of INVALID_CHALLENGE_ERROR.",
    "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
  ],
  [
    "The verificationMethod property of the proof MUST be a URL",
    "The verificationMethod property of the proof MUST be a URL."
  ],
  [
    "The type property of the proof MUST be DataIntegrityProof.",
    "The type property of the proof MUST be DataIntegrityProof."
  ],
  [
    "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3",
    "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3. Algorithms."
  ],
  [
    "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
    "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
  ],
  [
    "If the proofValue string does not start with u (U+0075, LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
    "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
  ],
  [
    "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)",
    "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)."
  ],
  [
    "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)",
    "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)."
  ],
  [
    "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR."
  ],
  [
    "When expressing a data integrity proof on an object, a proof property MUST be used",
    "When expressing a data integrity proof on an object, a proof property MUST be used."
  ],
  [
    "The reason the proof was created MUST be specified as a string that maps to a URL [URL]",
    "The reason the proof was created (\"proof.proofPurpose\") MUST be specified as a string that maps to a URL."
  ],
  [
    "If specified, its value MUST be a string.",
    "If specified (proof.cryptosuite), its value MUST be a string."
  ],
  [
    "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
    "When deserializing to RDF, implementations MUST ensure that the base URL is set to null."
  ],
  [
    "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite",
    "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite."
  ],
  [
    "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
    "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite."
  ],
  [
    "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR."
  ],
  [
    "Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Multikey.",
    "Dereferencing \"verificationMethod\" MUST result in an object containing a type property with \"Multikey\" value."
  ],
  [
    "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components",
    "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue."
  ],
  [
    "If the result is not an array of five, six, or seven elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
    "Initialize components to an array that is the result of CBOR-decoding the bytes that follow the three-byte BBS disclosure proof header. If the result is not an array of five or six elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
  ],
  [
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR."
  ],
  [
    "The cryptosuite property of the proof MUST be bbs-2023.",
    "The cryptosuite property of the proof MUST be bbs-2023."
  ],
  [
    "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
    "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
  ]
]
```
#### Unmatched Test Suite Statements
```json
[
  "(\"proof.id\") An optional identifier for the proof, which MUST be a URL.",
  "A verification method is the means and information needed to verify the proof. If included, the value MUST be a string that maps to a [URL].",
  "(\"proof.proofValue\") A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "the HMAC key MUST be the same length as the digest size",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "The cryptosuite property of the proof MUST be bbs-2023.",
  "The type property of the proof MUST be DataIntegrityProof.",
  "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3. Algorithms.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The verificationMethod property of the proof MUST be a URL.",
  "Dereferencing \"verificationMethod\" MUST result in an object containing a type property with \"Multikey\" value.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "the HMAC key MUST be the same length as the digest size",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "Initialize components to an array that is the result of CBOR-decoding the bytes that follow the three-byte BBS disclosure proof header. If the result is not an array of five or six elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "(\"proof.proofValue\") A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "(\"proof.proofValue\") A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite). A proof configuration object is produced as output.",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Whenever this algorithm (base proof) encodes strings, it MUST use UTF-8 encoding.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite). A proof configuration object is produced as output.",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR."
]
```
#### Unmatched Specifications Statements
```json
[
  "An optional identifier for the proof, which MUST be a URL [URL], such as a UUID as a URN (urn:uuid:6a1676b8-b51f-11ed-937b-d76685a20ff5)",
  "If included, the value MUST be a string that maps to a [URL]",
  "The date and time the proof was created is OPTIONAL and, if included, MUST be specified as an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC",
  "If present, it MUST be an [XMLSCHEMA11-2] dateTimeStamp string, either in Universal Coordinated Time (UTC), denoted by a Z at the end of the value, or with a time zone offset relative to UTC",
  "If specified, the associated value MUST be either a string, or an unordered set of strings",
  "The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data",
  "If present, it MUST be a string value or an unordered list of string values",
  "Each value identifies another data integrity proof, all of which MUST also verify for the current proof to be considered verified",
  "If present, the digestMultibase value MUST be a single string value, or an list of string values, each of which is a Multibase-encoded Multihash value.",
  "Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below:",
  "Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.",
  "Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document",
  "Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.",
  "However, if an @context declaration is not included, extensions (such as the addition of new properties) related to this specification or corresponding cryptosuites MUST NOT be made.",
  "The specification MUST be published as a human-readable document at a URL.",
  "The specification MUST identify a cryptographic suite type and any parameters that can be used with the suite.",
  "The specification MUST detail the transformation algorithms (if any), parameters, and other necessary details, used to modify input data into the data to be protected.",
  "The specification MUST detail the hashing algorithms parameters, and other necessary details used to perform cryptographic hashing to the data to be protected.",
  "The specification MUST detail the proof serialization algorithms, parameters, and other necessary details used to perform cryptographic protection of the data.",
  "The specification MUST detail the proof verification algorithms, parameters, and other necessary details used to perform cryptographic verification of the data.",
  "The specification MUST define a data integrity cryptographic suite instantiation algorithm that accepts a set of options (map options) and returns a cryptosuite instance (struct cryptosuite)",
  "The specification MUST detail any known resource starvation attack that can occur in an algorithm and provide testable mitigations against each attack.",
  "The specification MUST contain a Security Considerations section detailing security considerations specific to the cryptographic suite.",
  "The specification MUST contain a Privacy Considerations section detailing privacy considerations specific to the cryptographic suite.",
  "The JSON-LD context associated with the cryptographic suite MUST have its terms protected from unsafe redefinition, by use of the @protected keyword.",
  "If the processing environment supports string subtypes, the subtype of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype.",
  "If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.",
  "If one or more of the proof.type, proof.verificationMethod, and proof.proofPurpose values is not set, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "When a step says 'an error MUST be raised', it means that a verification result MUST be returned with a verified value of false and a non-empty errors list.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If domain was given, and it does not contain the same strings as proof.domain (treating a single string as a set containing just that string), an error MUST be raised and SHOULD convey an error type of INVALID_DOMAIN_ERROR.",
  "If a proof with id equal to previousProof does not exist in allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "If any element of previousProof list has an id attribute that does not match the id attribute of any element of allProofs, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The type value of the error object MUST be a URL that starts with the value https://w3id.org/security# and ends with the value in the section listed below.",
  "The code value MUST be the integer code described in the table below (in parentheses, beside the type name).",
  "Algorithms of this document MUST be enforced.",
  "Any other encodings MUST NOT be allowed.",
  "If featureOption is set to 'anonymous_holder_binding' or 'pseudonym_hidden_pid', the commitment_with_proof input MUST be supplied.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader",
  "Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.",
  "If featureOption is set to 'anonymous_holder_binding' or 'pseudonym_hidden_pid', the commitment_with_proof input MUST be supplied; if not supplied, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR",
  "If featureOption equals 'anonymous_holder_binding', the REQUIRED additional inputs are holderSecret and proverBlind",
  "If featureOption equals 'pseudonym_issuer_pid', the REQUIRED additional input is the verifier_id which is communicated to the holder by the verifier",
  "If featureOption equals 'pseudonym_hidden_pid', the REQUIRED additional inputs are the pid, proverBlind (both known to holder), and verifier_id which is communicated to the holder by the verifier"
]
```