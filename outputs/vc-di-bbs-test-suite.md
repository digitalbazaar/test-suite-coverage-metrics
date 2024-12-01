# Test Suite Coverage Metrics
## vc-di-bbs-test-suite
### Summary of normative statements coverage

| Count (Suite) | Count (Spec) | Matches | Unmatched (Suite) | Unmatched (Spec) |
| ------- | ------- | ------- | ------- | ------- |
| 80 | 26 | 16 |  64 |  10 |

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
  "The cryptosuite property of the proof MUST be bbs-2023.",
  "The type property of the proof MUST be DataIntegrityProof.",
  "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3. Algorithms.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The verificationMethod property of the proof MUST be a URL.",
  "Dereferencing 'verificationMethod' MUST result in an object containing a type property with 'Multikey' value.",
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
  "Dereferencing 'verificationMethod' MUST result in an object containing a type property with 'Multikey' value.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod).",
  "the HMAC key MUST be the same length as the digest size",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "Initialize components to an array that is the result of CBOR-decoding the bytes that follow the three-byte BBS disclosure proof header. If the result is not an array of five or six elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
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
  "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
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
  //! "The key words MAY, MUST, MUST NOT, OPTIONAL, REQUIRED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
  //! "Algorithms of this document MUST be enforced.",
  "Conforming processors MUST produce errors when non-conforming documents are consumed.",
  "Any other encodings MUST NOT be allowed.",
  // "The verificationMethod property of the proof MUST be a URL",
  //! "Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Multikey.",
  // "The type property of the proof MUST be DataIntegrityProof.",
  // "The cryptosuite property of the proof MUST be bbs-2023.",
  // "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3",
  // "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components",
  // "If the proofValue string does not start with u (U+0075 LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  // "If the decodedProofValue starts with any other three byte sequence, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  // "If the proofValue string does not start with u (U+0075, LATIN SMALL LETTER U), indicating that it is a multibase-base64url-no-pad-encoded value, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  // "If the result is not an array of five, six, or seven elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "If featureOption is set to 'anonymous_holder_binding' or 'pseudonym_hidden_pid', the commitment_with_proof input MUST be supplied.",
  // "The transformation options MUST contain a type identifier for the cryptographic suite (type), a cryptosuite identifier (cryptosuite), and a verification method (verificationMethod)",
  // "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers) and MAY contain additional options, such as a JSON-LD document loader",
  // "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
  // "Per the recommendations of [RFC2104], the HMAC key MUST be the same length as the digest size; for SHA-256, this is 256 bits or 32 bytes.",
  // "The proof options MUST contain a type identifier for the cryptographic suite (type) and MUST contain a cryptosuite identifier (cryptosuite)",
  // "If proofConfig.type is not set to DataIntegrityProof and/or proofConfig.cryptosuite is not set to bbs-2023, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  // "If proofConfig.created is set and if the value is not a valid [XMLSCHEMA11-2] datetime, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
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
    "The verificationMethod property of the proof MUST be a URL",
    "The verificationMethod property of the proof MUST be a URL."
  ],
  [
    "The type property of the proof MUST be DataIntegrityProof.",
    "The type property MUST contain the string DataIntegrityProof."
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
    "Whenever this algorithm encodes strings, it MUST use UTF-8 encoding.",
    "Whenever this algorithm (base proof) encodes strings, it MUST use UTF-8 encoding."
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
    "Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Multikey.",
    "Dereferencing 'verificationMethod' MUST result in an object containing a type property with 'Multikey' value."
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
  "The type property of the proof MUST be DataIntegrityProof.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "the HMAC key MUST be the same length as the digest size",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "The cryptosuite property of the proof MUST be bbs-2023.",
  "The type property of the proof MUST be DataIntegrityProof.",
  "The value of the proofValue property of the proof MUST be a BBS signature or BBS proof produced according to [CFRG-BBS-SIGNATURE] that is serialized and encoded according to procedures in section 3. Algorithms.",
  "A conforming proof is any concrete expression of the data model that complies with the normative statements in this specification. Specifically, all relevant normative statements in Sections 2. Data Model and 3. Algorithms of this document MUST be enforced.",
  "The verificationMethod property of the proof MUST be a URL.",
  "Dereferencing 'verificationMethod' MUST result in an object containing a type property with 'Multikey' value.",
  "The publicKeyMultibase property represents a Multibase-encoded Multikey expression of a BLS12-381 public key in the G2 group. The encoding of this field is the two-byte prefix 0xeb01 followed by the 96-byte compressed public key data. The 98-byte value is then encoded using base58-btc (z) as the prefix. Any other encodings MUST NOT be allowed.",
  "the HMAC key MUST be the same length as the digest size",
  "CBOR-encode components per [RFC8949] where CBOR tagging MUST NOT be used on any of the components. Append the produced encoded value to proofValue.",
  "The transformation options MUST contain an array of mandatory JSON pointers (mandatoryPointers)",
  "Initialize components to an array that is the result of CBOR-decoding the bytes that follow the three-byte BBS disclosure proof header. If the result is not an array of five or six elements \u2014 a byte array, a map of integers to integers, two arrays of integers, and one or two byte arrays; an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "When deserializing to RDF, implementations MUST ensure that the base URL is set to null.",
  "If either securedDocument is not a map or securedDocument.proof is not a map, an error MUST be raised and SHOULD convey an error type of PARSING_ERROR.",
  "If one or more of proof.type, proof.verificationMethod, and proof.proofPurpose does not exist, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR",
  "The type property MUST contain the string DataIntegrityProof.",
  "If expectedProofPurpose was given, and it does not match proof.proofPurpose, an error MUST be raised and SHOULD convey an error type of PROOF_VERIFICATION_ERROR.",
  "The proofValue property MUST be used, as specified in 2.1 Proofs.",
  "('proof.proofValue') A string value that contains the base-encoded binary data necessary to verify the digital proof using the verificationMethod specified. The contents of the value MUST be expressed with a header and encoding as described in Section 2.4 Multibase of the Controller Documents 1.0 specification.",
  "Implementations that use JSON-LD processing, such as RDF Dataset Canonicalization [RDF-CANON], MUST throw an error, which SHOULD be DATA_LOSS_DETECTION_ERROR, when data is dropped by a JSON-LD processor, such as when an undefined term is detected in an input document.",
  "The value of the cryptosuite property MUST be a string that identifies the cryptographic suite. If the processing environment supports subtypes of string, the type of the cryptosuite value MUST be the https://w3id.org/security#cryptosuiteString subtype of string.",
  "If options has a non-null domain item, it MUST be equal to proof.domain or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
  "If options has a non-null challenge item, it MUST be equal to proof.challenge or an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
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
  "The key words MAY, MUST, MUST NOT, OPTIONAL, REQUIRED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
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