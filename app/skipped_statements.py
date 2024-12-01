

SKIPPED_STATEMENTS = {
    "vc-di-ecdsa": [
        {
            "statement": "The key words MAY, MUST, MUST NOT, OPTIONAL, REQUIRED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
            "reason": "Generic term."
        },
        {
            "statement": "Algorithms of this document MUST be enforced.",
            "reason": "Generic term."
        },
    ],
    "vc-di-bbs": [
        {
            "statement": "The key words MAY, MUST, MUST NOT, OPTIONAL, REQUIRED, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
            "reason": ""
        },
        {
            "statement": "Algorithms of this document MUST be enforced.",
            "reason": ""
        },
        {
            "statement": "Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Multikey.",
            "reason": "DID Key"
        }
    ],
    "vc-data-integrity": [
        {
            "statement": "The key words MAY, MUST, MUST NOT, OPTIONAL, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
            "reason": ""
        },
        {
            "statement": "Implementations that perform JSON-LD processing MUST treat the following JSON-LD context URLs as already resolved, where the resolved document matches the corresponding hash values below:",
            "reason": ""
        },
        {
            "statement": "Implementations that perform RDF processing MUST treat the JSON-LD serialization of the vocabulary URL as already dereferenced, where the dereferenced document matches the corresponding hash value below.",
            "reason": ""
        },
        {
            "statement": "Applications MUST use the algorithm in Section 4.6 Context Validation, or one that achieves equivalent protections, to validate contexts in a conforming secured document",
            "reason": "Context validation, known contexts"
        },
        {
            "statement": "Context validation MUST be run after running the applicable algorithm in either Section 4.4 Verify Proof or Section 4.5 Verify Proof Sets and Chains.",
            "reason": "Context validation, known contexts"
        },
        {
            "statement": "However, if an @context declaration is not included, extensions (such as the addition of new properties) related to this specification or corresponding cryptosuites MUST NOT be made.",
            "reason": "Context validation, known contexts"
        },
        {
            "statement": "The specification MUST be published as a human-readable document at a URL.",
            "reason": ""
        },
        {
            "statement": "The specification MUST identify a cryptographic suite type and any parameters that can be used with the suite.",
            "reason": ""
        },
        {
            "statement": "The specification MUST detail the transformation algorithms (if any), parameters, and other necessary details, used to modify input data into the data to be protected.",
            "reason": ""
        },
        {
            "statement": "The specification MUST detail the hashing algorithms parameters, and other necessary details used to perform cryptographic hashing to the data to be protected.",
            "reason": ""
        },
        {
            "statement": "The specification MUST detail the proof serialization algorithms, parameters, and other necessary details used to perform cryptographic protection of the data.",
            "reason": ""
        },
        {
            "statement": "The specification MUST detail the proof verification algorithms, parameters, and other necessary details used to perform cryptographic verification of the data.",
            "reason": ""
        },
        {
            "statement": "The specification MUST define a data integrity cryptographic suite instantiation algorithm that accepts a set of options (map options) and returns a cryptosuite instance (struct cryptosuite)",
            "reason": ""
        },
        {
            "statement": "The specification MUST detail any known resource starvation attack that can occur in an algorithm and provide testable mitigations against each attack.",
            "reason": ""
        },
        {
            "statement": "The specification MUST contain a Security Considerations section detailing security considerations specific to the cryptographic suite.",
            "reason": ""
        },
        {
            "statement": "The specification MUST contain a Privacy Considerations section detailing privacy considerations specific to the cryptographic suite.",
            "reason": ""
        },
        {
            "statement": "The JSON-LD context associated with the cryptographic suite MUST have its terms protected from unsafe redefinition, by use of the @protected keyword.",
            "reason": ""
        }
    ],
    "vc-di-eddsa": [
        {
            "statement": "The key words MAY, MUST, MUST NOT, and SHOULD in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
            "reason": ""
        },
        {
            "statement": "Algorithms of this document MUST be enforced.",
            "reason": ""
        },
        {
            "statement": "The controller of the verification method MUST be a URL.",
            "reason": "Implicit with did key."
        },
        {
            "statement": "A Multibase-encoded Multikey value follows, which MUST consist of a binary value that starts with the two-byte prefix 0xed01, which is the Multikey header for an Ed25519 public key, followed by the 32-byte public key data, all of which is then encoded using base-58-btc",
            "reason": "Implicit with did key."
        },
        {
            "statement": "The secretKeyMultibase value of the verification method MUST start with the base-58-btc prefix (z), as defined in the Multibase section of Controller Documents 1.0",
            "reason": "secretKey"
        },
        {
            "statement": "The verificationMethod property of the proof MUST be a URL",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "Dereferencing the verificationMethod MUST result in an object containing a type property with the value set to Ed25519VerificationKey2020.",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "The type of the verification method MUST be Ed25519VerificationKey2020.",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "The type property of the proof MUST be Ed25519Signature2020.",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "The created property of the proof MUST be an [XMLSCHEMA11-2] formatted date string.",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "The proofPurpose property of the proof MUST be a string, and MUST match the verification relationship expressed by the verification method controller.",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "The proofValue property of the proof MUST be a detached EdDSA produced according to [RFC8032], encoded using the base-58-btc header and alphabet as described in the Multibase section of [VC-DATA-INTEGRITY].",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "To generate a proof, the algorithm in Section 4.1: Add Proof in the Data Integrity [VC-DATA-INTEGRITY] specification MUST be executed",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "To verify a proof, the algorithm in Section 4.2: Verify Proof in the Data Integrity [VC-DATA-INTEGRITY] specification MUST be executed",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "If options.type is not set to the string Ed25519Signature2020, an error MUST be raised that SHOULD convey an error type of PROOF_TRANSFORMATION_ERROR.",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "The proof configuration MUST contain a type identifier for the cryptographic suite (type) and MAY contain a cryptosuite identifier (cryptosuite)",
            "reason": "Ed25519Signature2020"
        },
        {
            "statement": "If proofConfig.type is not set to Ed25519Signature2020, an error MUST be raised and SHOULD convey an error type of PROOF_GENERATION_ERROR.",
            "reason": "Ed25519Signature2020"
        }
    ],
    "vc-bitstring-status-list": [
        {
            "statement": "The key words MAY, MUST, MUST NOT, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
            "reason": ""
        },
        {
            "statement": "While the value of the string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential",
            "reason": ""
        },
        {
            "statement": "If statusSize is not present as a property of the credentialStatus, then statusSize MUST be processed as 1",
            "reason": ""
        },
        {
            "statement": "One way to resolve this conflict is to remove ttl and specify that caching behavior can be expressed using protocol mechanisms (such as the expires header in HTTP), and that any caching performed MUST align with the validUntil value for the verifiable credential",
            "reason": ""
        },
        {
            "statement": "While the value of each string is arbitrary, the following values MUST be used for their intended purpose: Value Description revocation Used to cancel the validity of a verifiable credential",
            "reason": ""
        },
        {
            "statement": "If not present, implementers MUST use a value of 300000 for this property",
            "reason": ""
        },
        {
            "statement": "A verifier MUST NOT use a cached BitstringStatusListCredential that was cached for more than the ttl duration prior to the start of verification operation on a verifiable credential",
            "reason": ""
        },
    ],
    "vc-data-model-2.0": [
        {
            "statement": "The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.",
            "reason": ""
        },
        {
            "statement": "A conforming issuer implementation produces conforming documents, MUST include all required properties in the conforming documents it produces, and MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms.",
            "reason": ""
        },
        {
            "statement": "A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.",
            "reason": ""
        },
        {
            "statement": "A conforming document is a compacted JSON-LD document that complies with all of the relevant 'MUST' statements in this specification",
            "reason": ""
        },
        {
            "statement": "Specifically, the relevant normative 'MUST' statements in Sections 4",
            "reason": ""
        },
        {
            "statement": "Syntaxes of this document MUST be enforced",
            "reason": ""
        },
        {
            "statement": "A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp",
            "reason": ""
        },
        {
            "statement": "Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application",
            "reason": ""
        },
        {
            "statement": "Concerning this specification, the following table lists the objects that MUST have a type specified.",
            "reason": ""
        },
        {
            "statement": "Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject",
            "reason": ""
        },
        {
            "statement": "New terms MUST define a new URL for each term",
            "reason": ""
        },
        {
            "statement": "When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term",
            "reason": ""
        },
        {
            "statement": "Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.",
            "reason": ""
        },
        {
            "statement": "Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary",
            "reason": ""
        },
        {
            "statement": "This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value",
            "reason": ""
        },
        {
            "statement": "If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.",
            "reason": ""
        },
        {
            "statement": "A conforming verifier implementation that makes use of a resource based on the id of a relatedResource object inside a conforming document with a corresponding cryptographic digest appearing in a relatedResource object value MUST compute the digest of the retrieved resource",
            "reason": ""
        },
        {
            "statement": "Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.",
            "reason": ""
        },
        {
            "statement": "MUST identify whether the transformation to this data model is one-way-only or round-trippable.",
            "reason": ""
        },
        {
            "statement": "MUST preserve the @context values when performing round-trippable transformation.",
            "reason": ""
        },
        {
            "statement": "MUST result in a conforming document when transforming to the data model described by this specification.",
            "reason": ""
        },
        {
            "statement": "MUST specify a registered media type for the input document.",
            "reason": ""
        },
        {
            "statement": "Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents",
            "reason": ""
        },
        {
            "statement": "Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures",
            "reason": ""
        },
        {
            "statement": "A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData)",
            "reason": ""
        },
        {
            "statement": "A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph",
            "reason": ""
        },
        {
            "statement": "The securing mechanism MUST define all terms used by the proof graph",
            "reason": ""
        },
        {
            "statement": "The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.",
            "reason": ""
        },
        {
            "statement": "JSON-LD compacted document form MUST be used for all representations of the data model using the application/vc or application/vp media type.",
            "reason": ""
        },
        {
            "statement": "When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11]",
            "reason": ""
        },
        {
            "statement": "The language value object MUST NOT include any other keys beyond @value, @language, and @direction.",
            "reason": ""
        },
        {
            "statement": "Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 24a18c90e9856d526111f29376e302d970b2bd10182e33959995b0207d7043b9",
            "reason": ""
        },
        {
            "statement": "Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative",
            "reason": ""
        }
    ]
}