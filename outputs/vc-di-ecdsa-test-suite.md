# Test Suite Coverage Metrics
## vc-di-ecdsa-test-suite
### Summary of normative statements coverage

| Count (Suite) | Count (Spec) | Matches | Unmatched (Suite) | Unmatched (Spec) |
| ------- | ------- | ------- | ------- | ------- |
| 123 | 33 | 20 |  103 |  12 |

### Details
#### Test Suite Statements
```json
[
  "When expressing a data integrity proof on an object, a proof property MUST be used.",
  "If present (proof), its value MUST be either a single object, or an unordered set of objects.",
  "('proof.id') An optional identifier for the proof, which MUST be a URL.",
  "The specific type of proof MUST be specified as a string that maps to a URL.",
  "The type property MUST contain the string DataIntegrityProof.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.",
  "If specified (proof.cryptosuite), its value MUST be a string.",
  "A verification method is the means and information needed to verify the proof. If included, the value MUST be a string that maps to a [URL].",
  "The reason the proof was created ('proof.proofPurpose') MUST be specified as a string that maps to a URL.",
  "('proof.proofValue') A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data.",
  "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When expressing a data integrity proof on an object, a proof property MUST be used.",
  "If present (proof), its value MUST be either a single object, or an unordered set of objects.",
  "('proof.id') An optional identifier for the proof, which MUST be a URL.",
  "The specific type of proof MUST be specified as a string that maps to a URL.",
  "The type property MUST contain the string DataIntegrityProof.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.",
  "If specified (proof.cryptosuite), its value MUST be a string.",
  "A verification method is the means and information needed to verify the proof. If included, the value MUST be a string that maps to a [URL].",
  "The reason the proof was created ('proof.proofPurpose') MUST be specified as a string that maps to a URL.",
  "('proof.proofValue') A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data.",
  "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. ",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. ",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. ",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. ",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite).",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite).",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
  "If options.type is not set to the string DataIntegrityProof or options.cryptosuite is not set to the string ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite).",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite).",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding. (proof.type)",
  "If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised ",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite).",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite).",
  "When generating ECDSA signatures, the signature value MUST be expressed according to section 7 of [RFC4754] (sometimes referred to as the IEEE P1363 format) and encoded according to the specific cryptosuite proof generation algorithm.",
  "For P-256 keys, the default hashing function, SHA-2 with 256 bits of output, MUST be used.",
  "For P-384 keys, SHA-2 with 384-bits of output MUST be used, specified via the RDFC-1.0 implementation-specific parameter.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite).",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding. (proof.type)",
  "If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised ",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite).",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite).",
  "When generating ECDSA signatures, the signature value MUST be expressed according to section 7 of [RFC4754] (sometimes referred to as the IEEE P1363 format) and encoded according to the specific cryptosuite proof generation algorithm.",
  "For P-256 keys, the default hashing function, SHA-2 with 256 bits of output, MUST be used.",
  "For P-384 keys, SHA-2 with 384-bits of output MUST be used, specified via the RDFC-1.0 implementation-specific parameter."
]
```
#### Specifications Statements
```json
[
  "The key words MAY, MUST, MUST NOT, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
  "Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0",
  "Any other encoding MUST NOT be allowed.",
  "The secretKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "When generating ECDSA signatures, the signature value MUST be expressed according to section 7 of [RFC4754] (sometimes referred to as the IEEE P1363 format) and encoded according to the specific cryptosuite proof generation algorithm",
  "For P-256 keys, the default hashing function, SHA-2 with 256 bits of output, MUST be used",
  "For P-384 keys, SHA-2 with 384-bits of output MUST be used, specified via the RDFC-1.0 implementation-specific parameter.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
  "If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)",
  "If options.type is not set to the string DataIntegrityProof or options.cryptosuite is not set to the string ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "Note: All non-blank node identifiers in the path of any JSON Pointer MUST be included in the selection, this includes any root document identifier.",
  "Note: The selection MUST include all types in the path of any JSON Pointer, including any root document type.",
  "If value is now undefined, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR, indicating that the JSON pointer does not match the given document.",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components",
  "If the proofValue string does not start with u, indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the decodedProofValue does not start with the ECDSA-SD base proof header bytes 0xd9, 0x5d, and 0x00, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the decodedProofValue does not start with the ECDSA-SD disclosure proof header bytes 0xd9, 0x5d, and 0x01, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the result is not an array of the following five elements \u2014 a byte array of length 64; a byte array of length 36; an array of byte arrays, each of length 64; a map of integers to byte arrays, each of length 32; and an array of integers \u2014 an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader",
  "Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.",
  "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-sd-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If the length of signatures does not match the length of nonMandatory, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR, indicating that the signature count does not match the non-mandatory message count."
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
    "Any other encoding MUST NOT be allowed.",
    "Any other encoding MUST NOT be allowed. (verificationMethod)"
  ],
  [
    "The type property MUST be DataIntegrityProof.",
    "The type property MUST contain the string DataIntegrityProof."
  ],
  [
    "When generating ECDSA signatures, the signature value MUST be expressed according to section 7 of [RFC4754] (sometimes referred to as the IEEE P1363 format) and encoded according to the specific cryptosuite proof generation algorithm",
    "When generating ECDSA signatures, the signature value MUST be expressed according to section 7 of [RFC4754] (sometimes referred to as the IEEE P1363 format) and encoded according to the specific cryptosuite proof generation algorithm."
  ],
  [
    "For P-384 keys, SHA-2 with 384-bits of output MUST be used, specified via the RDFC-1.0 implementation-specific parameter.",
    "For P-384 keys, SHA-2 with 384-bits of output MUST be used, specified via the RDFC-1.0 implementation-specific parameter."
  ],
  [
    "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
    "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding."
  ],
  [
    "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)",
    "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)."
  ],
  [
    "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR."
  ],
  [
    "If options.type is not set to the string DataIntegrityProof or options.cryptosuite is not set to the string ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.",
    "If options.type is not set to the string DataIntegrityProof or options.cryptosuite is not set to the string ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR."
  ],
  [
    "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)",
    "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)."
  ],
  [
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-sd-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR."
  ],
  [
    "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0",
    "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. "
  ],
  [
    "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
    "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023."
  ],
  [
    "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)",
    "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)."
  ],
  [
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised"
  ],
  [
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-jcs-2019, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
    "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to ecdsa-rdfc-2019, an error MUST be raised"
  ],
  [
    "The secretKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0",
    "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. "
  ],
  [
    "If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised and SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.",
    "If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised "
  ],
  [
    "For P-256 keys, the default hashing function, SHA-2 with 256 bits of output, MUST be used",
    "For P-256 keys, the default hashing function, SHA-2 with 256 bits of output, MUST be used."
  ],
  [
    "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)",
    "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite)."
  ]
]
```
#### Unmatched Test Suite Statements
```json
[
  "When expressing a data integrity proof on an object, a proof property MUST be used.",
  "If present (proof), its value MUST be either a single object, or an unordered set of objects.",
  "('proof.id') An optional identifier for the proof, which MUST be a URL.",
  "The specific type of proof MUST be specified as a string that maps to a URL.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.",
  "If specified (proof.cryptosuite), its value MUST be a string.",
  "A verification method is the means and information needed to verify the proof. If included, the value MUST be a string that maps to a [URL].",
  "The reason the proof was created ('proof.proofPurpose') MUST be specified as a string that maps to a URL.",
  "('proof.proofValue') A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data.",
  "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When expressing a data integrity proof on an object, a proof property MUST be used.",
  "If present (proof), its value MUST be either a single object, or an unordered set of objects.",
  "('proof.id') An optional identifier for the proof, which MUST be a URL.",
  "The specific type of proof MUST be specified as a string that maps to a URL.",
  "The type property MUST contain the string DataIntegrityProof.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "If the proof type is DataIntegrityProof, cryptosuite MUST be specified; otherwise, cryptosuite MAY be specified.",
  "If specified (proof.cryptosuite), its value MUST be a string.",
  "A verification method is the means and information needed to verify the proof. If included, the value MUST be a string that maps to a [URL].",
  "The reason the proof was created ('proof.proofPurpose') MUST be specified as a string that maps to a URL.",
  "('proof.proofValue') A string value that expresses base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The value MUST use a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification to express the binary data.",
  "Cryptographic suite designers MUST use mandatory proof value properties defined in Section 2.1 Proofs, and MAY define other properties specific to their cryptographic suite.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "If the algorithm produces an error, the error MUST be propagated and SHOULD convey the error type.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "The type property MUST be DataIntegrityProof.",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. ",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "The publicKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0. ",
  "Any other encoding MUST NOT be allowed. (verificationMethod)",
  "The type property MUST be DataIntegrityProof.",
  "The cryptosuite property MUST be ecdsa-rdfc-2019, ecdsa-jcs-2019, or ecdsa-sd-2023.",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding. (proof.type)",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite).",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite).",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type) and a cryptosuite identifier (cryptosuite).",
  "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding. (proof.type)",
  "If options.type is not set to the string DataIntegrityProof and options.cryptosuite is not set to the string ecdsa-rdfc-2019, an error MUST be raised ",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite).",
  "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised",
  "The proof options MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite).",
  "When generating ECDSA signatures, the signature value MUST be expressed according to section 7 of [RFC4754] (sometimes referred to as the IEEE P1363 format) and encoded according to the specific cryptosuite proof generation algorithm.",
  "For P-256 keys, the default hashing function, SHA-2 with 256 bits of output, MUST be used.",
  "For P-384 keys, SHA-2 with 384-bits of output MUST be used, specified via the RDFC-1.0 implementation-specific parameter."
]
```
#### Unmatched Specifications Statements
```json
[
  "The key words MAY, MUST, MUST NOT, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
  "Note: All non-blank node identifiers in the path of any JSON Pointer MUST be included in the selection, this includes any root document identifier.",
  "Note: The selection MUST include all types in the path of any JSON Pointer, including any root document type.",
  "If value is now undefined, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR, indicating that the JSON pointer does not match the given document.",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components",
  "If the proofValue string does not start with u, indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the decodedProofValue does not start with the ECDSA-SD base proof header bytes 0xd9, 0x5d, and 0x00, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the decodedProofValue does not start with the ECDSA-SD disclosure proof header bytes 0xd9, 0x5d, and 0x01, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If the result is not an array of the following five elements \u2014 a byte array of length 64; a byte array of length 36; an array of byte arrays, each of length 64; a map of integers to byte arrays, each of length 32; and an array of integers \u2014 an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader",
  "Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.",
  "If the length of signatures does not match the length of nonMandatory, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR, indicating that the signature count does not match the non-mandatory message count."
]
```