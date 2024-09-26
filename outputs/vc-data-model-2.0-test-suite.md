# Test Suite Coverage Metrics
## vc-data-model-2.0-test-suite

### Summary of supported features and implementations

*This highlights features that have less than 2 passing implementations.*

| Risk Score | Failed % | Failed Count | Total Count |
| ------- | ------- | ------- | ------- |
| Medium | 7 | 5 |  64 |

#### Details
*Features with a state of pending are not considered at risk.*

##### At Risk Features

- The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification.
- The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].
- The type value of the object MUST be EnvelopedVerifiableCredential.
- The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers. The value MUST be unique among the list of related resource objects.
- Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.

##### Pending Features

- A conforming verifier implementation MUST check that each required property satisfies the normative requirementsfor that property.
- Time values that are incorrectly serialized without an offset MUST be interpreted as UTC.
- Credential status specifications MUST NOT enable tracking of individuals
- If [the `id` field is] present, the normative guidance in Section 4.4 Identifiers MUST be followed.
- A verifiable presentation that includes a self-asserted verifiable credential that is only secured using the same mechanism as the verifiable presentation MUST include a holder property.
- When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation.
- The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification.
- The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].
- The type value of the object MUST be EnvelopedVerifiablePresentation.
- In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property.

### Summary of normative statements coverage

| Count (Suite) | Count (Spec) | Matches | Unmatched (Suite) | Unmatched (Spec) |
| ------- | ------- | ------- | ------- | ------- |
| 64 | 89 | 38 |  26 |  51 |

### Details
#### Test Suite Statements
```json
[
  "A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.",
  "A conforming issuer implementation MUST include all required properties in the conforming documents it produces.",
  "A conforming issuer implementation MUST secure the conforming documents it produces using a securing mechanismdescribed in Section 4.12 Securing Mechanisms.",
  "A conforming verifier implementation MUST perform verification on a conforming document as described inSection 4.12 Securing Mechanisms.",
  "A conforming verifier implementation MUST check that each required property satisfies the normative requirementsfor that property.",
  "A conforming verifier implementation MUST produce errors when non-conforming documents are detected.",
  "Verifiable credentials MUST include a @context property.",
  "Verifiable presentations MUST include a @context property.",
  "Verifiable credentials: The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2.",
  "Verifiable presentations: The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2.",
  "Verifiable Credential `@context`: \"Subsequent items in the ordered set MUST be composed of any combination of URLs and/or objects where each is processable as a JSON-LD Context.\"",
  "Verifiable Presentation `@context`: \"Subsequent items in the ordered set MUST be composed of any combination of URLs and/or objects where each is processable as a JSON-LD Context.\"",
  "If present, the value of the id property MUST be a single URL, which MAY be dereferenceable.",
  "Verifiable credentials MUST contain a type property with an associated value.",
  "Verifiable presentations MUST contain a type property with an associated value.",
  "The value of the type property MUST be one or more terms and/or absolute URL strings.",
  "If more than one (type) value is provided, the order does not matter.",
  "Verifiable Credential objects MUST have a type specified.",
  "Verifiable Presentation objects MUST have a type specified.",
  "`credentialStatus` objects MUST have a type specified.",
  "`termsOfUse` objects MUST have a type specified.",
  "`evidence` objects MUST have a type specified.",
  "`refreshService` objects MUST have a type specified.",
  "`credentialSchema` objects MUST have a type specified.",
  "If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction.",
  "If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction.",
  "If present (on `issuer`), the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction.",
  "If present (on `issuer`), the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction.",
  "A verifiable credential MUST have an issuer property.",
  "The value of the issuer property MUST be either a URL, or an object containing an id property whose value is a URL.",
  "A verifiable credential MUST contain a credentialSubject property.",
  "The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property.",
  "If present, the value of the validFrom property MUST be an [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or in the past.",
  "If present, the value of the validUntil property MUST be an [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or in the future.",
  "If a validUntil value also exists, the validFrom value MUST express a datetime that is temporally the same or earlier than the datetime expressed by the validUntil value.",
  "If a validFrom value also exists, the validUntil value MUST express a datetime that is temporally the same or later than the datetime expressed by the validFrom value.",
  "Time values that are incorrectly serialized without an offset MUST be interpreted as UTC.",
  "If present (credentialStatus.id), the normative guidance in Section 4.4 Identifiers MUST be followed.",
  "(If a credentialStatus property is present), The type property is REQUIRED. It is used to express the type of status information expressed by the object. The related normative guidance in Section 4.5 Types MUST be followed.",
  "Credential status specifications MUST NOT enable tracking of individuals",
  "The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s).",
  "Each credentialSchema MUST specify its type (for example, JsonSchema), and an id property that MUST be a URL identifying the schema file.",
  "If multiple schemas are present, validity is determined according to the processing rules outlined by each associated type property",
  "If [the `id` field is] present, the normative guidance in Section 4.4 Identifiers MUST be followed.",
  "The type property MUST be present. One value of this property MUST be VerifiablePresentation, but additional types MAY be included.The related normative guidance in Section 4.5 Types MUST be followed.",
  "The verifiableCredential property MAY be present. The value MUST beone or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs).",
  "A verifiable presentation that includes a self-asserted verifiable credential that is only secured using the same mechanism as the verifiable presentation MUST include a holder property.",
  "When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation.",
  "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification.",
  "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].",
  "The type value of the object MUST be EnvelopedVerifiableCredential.",
  "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification.",
  "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE].",
  "The type value of the object MUST be EnvelopedVerifiablePresentation.",
  "When processing the active context defined by the base JSON-LD Context document defined in this specification, compliant JSON-LD-based processors produce an error when a JSON-LD context redefines any term.",
  "The value of the relatedResource property MUST be one or more objects of the following form:",
  "The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers. The value MUST be unique among the list of related resource objects.",
  "Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.",
  "The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential.",
  "Each refreshService value MUST specify its type.",
  "The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation.",
  "Each termsOfUse value MUST specify its type, for example, IssuerPolicy, and MAY specify its instance id.",
  "If present, the value associated with the evidence property is a single object or a set of one or more objects.",
  "In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property."
]
```
#### Specifications Statements
```json
[
  "A conforming document is a compacted JSON-LD document that complies with all of the relevant 'MUST' statements in this specification",
  "Specifically, the relevant normative 'MUST' statements in Sections 4",
  "Syntaxes of this document MUST be enforced",
  "A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp",
  "A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.",
  "A conforming issuer implementation produces conforming documents, MUST include all required properties in the conforming documents it produces, and MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms.",
  "A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.",
  "Verifiable credentials and verifiable presentations MUST include a @context property",
  "Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application",
  "The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2",
  "Subsequent items in the ordered set MUST be composed of any combination of URLs and objects, where each is processable as a JSON-LD Context.",
  "If present, id property's value MUST be a single URL, which MAY be dereferenceable",
  "Verifiable credentials and verifiable presentations MUST contain a type property with an associated value.",
  "The value of the type property MUST be one or more terms and absolute URL strings",
  "Concerning this specification, the following table lists the objects that MUST have a type specified.",
  "If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction",
  "If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction",
  "A verifiable credential MUST have an issuer property.",
  "The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL; in either case, the issuer selects this URL to identify itself in a globally unambiguous way",
  "A verifiable credential MUST contain a credentialSubject property.",
  "The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property",
  "If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past",
  "If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value.",
  "If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future",
  "If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.",
  "If present, the normative guidance in Section 4.4 Identifiers MUST be followed.",
  "The type property is REQUIRED",
  "The related normative guidance in Section 4.5 Types MUST be followed.",
  "Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject",
  "The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s)",
  "Each credentialSchema MUST specify its type (for example, JsonSchema) and an id property that MUST be a URL identifying the schema file",
  "The type property MUST be present",
  "One value of this property MUST be VerifiablePresentation, but additional types MAY be included",
  "The value MUST be one or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs)",
  "These objects are called verifiable credential graphs and MUST express information that is secured using a securing mechanism",
  "If present, the value MUST be either a URL or an object containing an id property",
  "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification",
  "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]",
  "The type value of the object MUST be EnvelopedVerifiableCredential.",
  "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification",
  "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]",
  "The type value of the object MUST be EnvelopedVerifiablePresentation.",
  "A verifiable presentation that includes a self-asserted verifiable credential, which is secured only using the same mechanism as the verifiable presentation, MUST include a holder property.",
  "When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation.",
  "New terms MUST define a new URL for each term",
  "When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term",
  "Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.",
  "Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary",
  "This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value",
  "If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.",
  "The value of the relatedResource property MUST be one or more objects of the following form: Property Description id The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers",
  "The value MUST be unique among the list of related resource objects",
  "Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.",
  "The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers",
  "The value MUST be unique among the list of related resource objects.",
  "If it is, the specification MUST produce a validation error unless the resource matches the expected media type and cryptographic digest.",
  "The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential",
  "Each refreshService value MUST specify its type",
  "The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation",
  "Each termsOfUse value MUST specify its type, for example, TrustFrameworkPolicy, and MAY specify its instance id",
  "If present, the value of the evidence property MUST be either a single object or a set of one or more objects",
  "If present, the normative guidance in Section 4.4 Identifiers MUST be followed",
  "type The type property is REQUIRED",
  "Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.",
  "Time values that are incorrectly serialized without an offset MUST be interpreted as UTC",
  "In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property",
  "The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#confidenceMethod.",
  "The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#renderMethod.",
  "MUST identify whether the transformation to this data model is one-way-only or round-trippable.",
  "MUST preserve the @context values when performing round-trippable transformation.",
  "MUST result in a conforming document when transforming to the data model described by this specification.",
  "MUST specify a registered media type for the input document.",
  "Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents",
  "Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures",
  "A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData)",
  "A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph",
  "The securing mechanism MUST define all terms used by the proof graph",
  "The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.",
  "JSON-LD compacted document form MUST be utilized for all representations of the data model using the application/vc or application/vp media type.",
  "This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation",
  "The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.",
  "The type property MUST be present and its value MUST be a URL identifying the type of problem.",
  "The title property MUST be present and its value SHOULD provide a short but specific human-readable string for the problem.",
  "The detail property MUST be present and its value SHOULD provide a longer human-readable string for the problem.",
  "When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11]",
  "The language value object MUST NOT include any other keys beyond @value, @language, and @direction.",
  "Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 24a18c90e9856d526111f29376e302d970b2bd10182e33959995b0207d7043b9",
  "If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.",
  "Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative"
]
```
#### Matched Statements
```json
[
  [
    "A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms.",
    "A conforming document MUST be secured by at least one securing mechanism as described in Section 4.12 Securing Mechanisms."
  ],
  [
    "Verifiable credentials and verifiable presentations MUST include a @context property",
    "Verifiable credentials MUST include a @context property."
  ],
  [
    "The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2",
    "Verifiable credentials: The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2."
  ],
  [
    "If present, id property's value MUST be a single URL, which MAY be dereferenceable",
    "If present, the value of the id property MUST be a single URL, which MAY be dereferenceable."
  ],
  [
    "The value of the type property MUST be one or more terms and absolute URL strings",
    "The value of the type property MUST be one or more terms and/or absolute URL strings."
  ],
  [
    "If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction",
    "If present, the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction."
  ],
  [
    "A verifiable credential MUST have an issuer property.",
    "A verifiable credential MUST have an issuer property."
  ],
  [
    "A verifiable credential MUST contain a credentialSubject property.",
    "A verifiable credential MUST contain a credentialSubject property."
  ],
  [
    "If present, the value of the validFrom property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or the past",
    "If present, the value of the validFrom property MUST be an [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential becomes valid, which could be a date and time in the future or in the past."
  ],
  [
    "If present, the value of the validUntil property MUST be a [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or the future",
    "If present, the value of the validUntil property MUST be an [XMLSCHEMA11-2] dateTimeStamp string value representing the date and time the credential ceases to be valid, which could be a date and time in the past or in the future."
  ],
  [
    "If present, the normative guidance in Section 4.4 Identifiers MUST be followed.",
    "If present (credentialStatus.id), the normative guidance in Section 4.4 Identifiers MUST be followed."
  ],
  [
    "The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s)",
    "The value of the credentialSchema property MUST be one or more data schemas that provide verifiers with enough information to determine whether the provided data conforms to the provided schema(s)."
  ],
  [
    "The value MUST be one or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs)",
    "The verifiableCredential property MAY be present. The value MUST beone or more verifiable credential and/or enveloped verifiable credential objects (the values MUST NOT be non-object values such as numbers, strings, or URLs)."
  ],
  [
    "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification",
    "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiableCredential terms as defined by the base context provided by this specification."
  ],
  [
    "The type value of the object MUST be EnvelopedVerifiableCredential.",
    "The type value of the object MUST be EnvelopedVerifiableCredential."
  ],
  [
    "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]",
    "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]."
  ],
  [
    "A verifiable presentation that includes a self-asserted verifiable credential, which is secured only using the same mechanism as the verifiable presentation, MUST include a holder property.",
    "A verifiable presentation that includes a self-asserted verifiable credential that is only secured using the same mechanism as the verifiable presentation MUST include a holder property."
  ],
  [
    "Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value.",
    "Each object associated with relatedResource MUST contain at least a digestSRI or a digestMultibase value."
  ],
  [
    "The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential",
    "The value of the refreshService property MUST be one or more refresh services that provides enough information to the recipient's software such that the recipient can refresh the verifiable credential."
  ],
  [
    "The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation",
    "The value of the termsOfUse property MUST specify one or more terms of use policies under which the creator issued the credential or presentation."
  ],
  [
    "If present, the value of the evidence property MUST be either a single object or a set of one or more objects",
    "If present, the value associated with the evidence property is a single object or a set of one or more objects."
  ],
  [
    "Time values that are incorrectly serialized without an offset MUST be interpreted as UTC",
    "Time values that are incorrectly serialized without an offset MUST be interpreted as UTC."
  ],
  [
    "Subsequent items in the ordered set MUST be composed of any combination of URLs and objects, where each is processable as a JSON-LD Context.",
    "Verifiable Credential `@context`: \"Subsequent items in the ordered set MUST be composed of any combination of URLs and/or objects where each is processable as a JSON-LD Context.\""
  ],
  [
    "If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction",
    "If present, the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction."
  ],
  [
    "The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property",
    "The value of the credentialSubject property is a set of objects where each object MUST be the subject of one or more claims, which MUST be serialized inside the credentialSubject property."
  ],
  [
    "If a validFrom value also exists, the validUntil value MUST express a point in time that is temporally the same or later than the point in time expressed by the validFrom value.",
    "If a validUntil value also exists, the validFrom value MUST express a datetime that is temporally the same or earlier than the datetime expressed by the validUntil value."
  ],
  [
    "Each credentialSchema MUST specify its type (for example, JsonSchema) and an id property that MUST be a URL identifying the schema file",
    "Each credentialSchema MUST specify its type (for example, JsonSchema), and an id property that MUST be a URL identifying the schema file."
  ],
  [
    "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable credential using an enveloping security scheme, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]",
    "The id value of the object MUST be a data: URL [RFC2397] that expresses a secured verifiable presentation using an enveloping securing mechanism, such as Securing Verifiable Credentials using JOSE and COSE [VC-JOSE-COSE]."
  ],
  [
    "The type value of the object MUST be EnvelopedVerifiablePresentation.",
    "The type value of the object MUST be EnvelopedVerifiablePresentation."
  ],
  [
    "The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers",
    "The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers. The value MUST be unique among the list of related resource objects."
  ],
  [
    "Each refreshService value MUST specify its type",
    "Each refreshService value MUST specify its type."
  ],
  [
    "If present, the normative guidance in Section 4.4 Identifiers MUST be followed",
    "If [the `id` field is] present, the normative guidance in Section 4.4 Identifiers MUST be followed."
  ],
  [
    "In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property",
    "In order to avoid collisions regarding how the following properties are used, implementations MUST specify a type property in the value associated with the reserved property."
  ],
  [
    "Verifiable credentials and verifiable presentations MUST contain a type property with an associated value.",
    "Verifiable credentials MUST contain a type property with an associated value."
  ],
  [
    "If a validUntil value also exists, the validFrom value MUST express a point in time that is temporally the same or earlier than the point in time expressed by the validUntil value.",
    "If a validFrom value also exists, the validUntil value MUST express a datetime that is temporally the same or later than the datetime expressed by the validFrom value."
  ],
  [
    "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification",
    "The @context property of the object MUST be present and include a context, such as the base context for this specification, that defines at least the id, type, and EnvelopedVerifiablePresentation terms as defined by the base context provided by this specification."
  ],
  [
    "Each termsOfUse value MUST specify its type, for example, TrustFrameworkPolicy, and MAY specify its instance id",
    "Each termsOfUse value MUST specify its type, for example, IssuerPolicy, and MAY specify its instance id."
  ],
  [
    "When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation.",
    "When a self-asserted verifiable credential is secured using the same mechanism as the verifiable presentation, the value of the issuer property of the verifiable credential MUST be identical to the holder property of the verifiable presentation."
  ]
]
```
#### Unmatched Test Suite Statements
```json
[
  "A conforming issuer implementation MUST include all required properties in the conforming documents it produces.",
  "A conforming issuer implementation MUST secure the conforming documents it produces using a securing mechanismdescribed in Section 4.12 Securing Mechanisms.",
  "A conforming verifier implementation MUST perform verification on a conforming document as described inSection 4.12 Securing Mechanisms.",
  "A conforming verifier implementation MUST check that each required property satisfies the normative requirementsfor that property.",
  "A conforming verifier implementation MUST produce errors when non-conforming documents are detected.",
  "Verifiable presentations MUST include a @context property.",
  "Verifiable presentations: The value of the @context property MUST be an ordered set where the first item is a URL with the value https://www.w3.org/ns/credentials/v2.",
  "Verifiable Presentation `@context`: \"Subsequent items in the ordered set MUST be composed of any combination of URLs and/or objects where each is processable as a JSON-LD Context.\"",
  "Verifiable presentations MUST contain a type property with an associated value.",
  "If more than one (type) value is provided, the order does not matter.",
  "Verifiable Credential objects MUST have a type specified.",
  "Verifiable Presentation objects MUST have a type specified.",
  "`credentialStatus` objects MUST have a type specified.",
  "`termsOfUse` objects MUST have a type specified.",
  "`evidence` objects MUST have a type specified.",
  "`refreshService` objects MUST have a type specified.",
  "`credentialSchema` objects MUST have a type specified.",
  "If present (on `issuer`), the value of the name property MUST be a string or a language value object as described in 11.1 Language and Base Direction.",
  "If present (on `issuer`), the value of the description property MUST be a string or a language value object as described in 11.1 Language and Base Direction.",
  "The value of the issuer property MUST be either a URL, or an object containing an id property whose value is a URL.",
  "(If a credentialStatus property is present), The type property is REQUIRED. It is used to express the type of status information expressed by the object. The related normative guidance in Section 4.5 Types MUST be followed.",
  "Credential status specifications MUST NOT enable tracking of individuals",
  "If multiple schemas are present, validity is determined according to the processing rules outlined by each associated type property",
  "The type property MUST be present. One value of this property MUST be VerifiablePresentation, but additional types MAY be included.The related normative guidance in Section 4.5 Types MUST be followed.",
  "When processing the active context defined by the base JSON-LD Context document defined in this specification, compliant JSON-LD-based processors produce an error when a JSON-LD context redefines any term.",
  "The value of the relatedResource property MUST be one or more objects of the following form:"
]
```
#### Unmatched Specifications Statements
```json
[
  "A conforming document is a compacted JSON-LD document that complies with all of the relevant 'MUST' statements in this specification",
  "Specifically, the relevant normative 'MUST' statements in Sections 4",
  "Syntaxes of this document MUST be enforced",
  "A conforming document MUST be either a verifiable credential with a media type of application/vc or a verifiable presentation with a media type of application/vp",
  "A conforming issuer implementation produces conforming documents, MUST include all required properties in the conforming documents it produces, and MUST secure the conforming documents it produces using a securing mechanism described in Section 4.12 Securing Mechanisms.",
  "A conforming verifier implementation consumes conforming documents, MUST perform verification on a conforming document as described in Section 4.12 Securing Mechanisms, MUST check that each required property satisfies the normative requirements for that property, and MUST produce errors when non-conforming documents are detected.",
  "Application developers MUST understand every JSON-LD context used by their application, at least to the extent that it affects the meaning of the terms used by their application",
  "Concerning this specification, the following table lists the objects that MUST have a type specified.",
  "The value of the issuer property MUST be either a URL or an object containing an id property whose value is a URL; in either case, the issuer selects this URL to identify itself in a globally unambiguous way",
  "The type property is REQUIRED",
  "The related normative guidance in Section 4.5 Types MUST be followed.",
  "Credential status specifications MUST NOT enable tracking of individuals, such as an issuer being notified (either directly or indirectly) when a verifier is interested in a specific holder or subject",
  "The type property MUST be present",
  "One value of this property MUST be VerifiablePresentation, but additional types MAY be included",
  "These objects are called verifiable credential graphs and MUST express information that is secured using a securing mechanism",
  "If present, the value MUST be either a URL or an object containing an id property",
  "New terms MUST define a new URL for each term",
  "When doing so, the general guidelines for [LINKED-DATA] are expected to be followed, in particular: Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term",
  "Human-readable documentation MUST be published, describing the semantics of and the constraints on the use of each term.",
  "Furthermore, a machine-readable description (that is, a JSON-LD Context document) MUST be published at the URL specified in the @context property for the vocabulary",
  "This context MUST map each term to its corresponding URL, possibly accompanied by further constraints like the type of the property value",
  "If a conforming document does not use JSON-LD Contexts that define all terms used, it MUST include the https://www.w3.org/ns/credentials/undefined-terms/v2 as the last value in the @context property.",
  "The value of the relatedResource property MUST be one or more objects of the following form: Property Description id The identifier for the resource is REQUIRED and conforms to the format defined in Section 4.4 Identifiers",
  "The value MUST be unique among the list of related resource objects",
  "The value MUST be unique among the list of related resource objects.",
  "If it is, the specification MUST produce a validation error unless the resource matches the expected media type and cryptographic digest.",
  "type The type property is REQUIRED",
  "Specification authors that create securing mechanisms MUST NOT design them in such a way that they leak information that would enable the verifier to correlate a holder across multiple verifiable presentations to different verifiers.",
  "The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#confidenceMethod.",
  "The associated vocabulary URL MUST be https://www.w3.org/2018/credentials#renderMethod.",
  "MUST identify whether the transformation to this data model is one-way-only or round-trippable.",
  "MUST preserve the @context values when performing round-trippable transformation.",
  "MUST result in a conforming document when transforming to the data model described by this specification.",
  "MUST specify a registered media type for the input document.",
  "Securing mechanism specifications MUST document normative algorithms that provide content integrity protection for conforming documents",
  "Securing mechanism specifications MUST provide a verification algorithm that returns the information in the conforming document that has been secured, in isolation, without including any securing mechanism information, such as proof or JOSE/COSE header parameters and signatures",
  "A verification algorithm MUST provide an interface that receives a media type (string inputMediaType) and input data (byte sequence or map inputData)",
  "A securing mechanism specification that creates a new type of embedded proof MUST specify a property that relates the verifiable credential or verifiable presentation to a proof graph",
  "The securing mechanism MUST define all terms used by the proof graph",
  "The securing mechanism MUST secure all graphs in the verifiable credential or the verifiable presentation, except for any proof graphs securing the verifiable credential or the verifiable presentation itself.",
  "JSON-LD compacted document form MUST be utilized for all representations of the data model using the application/vc or application/vp media type.",
  "This section contains an algorithm that conforming verifier implementations MUST run when verifying a verifiable credential or a verifiable presentation",
  "The verifyProof function MUST implement the interface described in 5.13 Securing Mechanism Specifications.",
  "The type property MUST be present and its value MUST be a URL identifying the type of problem.",
  "The title property MUST be present and its value SHOULD provide a short but specific human-readable string for the problem.",
  "The detail property MUST be present and its value SHOULD provide a longer human-readable string for the problem.",
  "When the language value object is used in place of a string value, the object MUST contain a @value property whose value is a string, and SHOULD contain a @language property whose value is a string containing a well-formed Language-Tag as defined by [BCP47], and MAY contain a @direction property whose value is a base direction string defined by the @direction property in [JSON-LD11]",
  "The language value object MUST NOT include any other keys beyond @value, @language, and @direction.",
  "Implementations MUST treat the base context value, located at https://www.w3.org/ns/credentials/v2, as already retrieved; the following value is the hexadecimal encoded SHA2-256 digest value of the base context file: 24a18c90e9856d526111f29376e302d970b2bd10182e33959995b0207d7043b9",
  "If such operations are performed and result in an error, the verifiable credential or verifiable presentation MUST result in a verification failure.",
  "Implementations that depend on RDF vocabulary processing MUST ensure that the following vocabulary URLs used in the base context ultimately resolve to the following files when loading the JSON-LD serializations, which are normative"
]
```