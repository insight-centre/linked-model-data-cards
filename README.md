# Bias Detection with A Semantic Approach for Linked Model, Data, and Dataspace Cards

In the realm of artificial intelligence, the significance of thorough documentation is often underestimated by practitioners during the development and publishing of models and datasets. However, due to the recent trend in the explainability and fairness of AI models, several frameworks have been proposed such as Model Cards, and Data Cards, among others, to help in the appropriate re-usage of those models and datasets. Moreover, the introduction of the dataspace concept offers possibilities of integration of Model Cards, Data Cards, and Service Cards, into Dataspace Cards. The Dataspace card serves as a comprehensive framework for systematically capturing and organizing crucial information for better decision-making about which model and data can be used for a specific application. This paper advocates for the adoption of a Semantic Web approach for transforming Model/Data Cards into Linked Data or knowledge graphs within a dataspace, rendering them machine-readable and interoperable. A significant contribution is the development of a vocabulary enabling linking between Data card, model card and dataspace card ontology, enhancing consistent documentation and understanding of Dataspace design. This helps in building trust and reuse of models and data among companies and individuals participating as publishers or consumers of such assets. The paper further demonstrates the applicability of the proposed schema in various use cases including bias detection in BERT-base-uncased and Large Language Model (GPT-4). Such work can be extended by conducting an in-depth examination of the proposed schema and Dataspace Cards for a specific use case, such as sentiment and emotion analysis, to further enhance their practical applicability.

--------------

This repository contains the proposals made under _Bias Detection with A Semantic Approach for Linked Model, Data, and 
Dataspace Cards_. 

The following directories contain the schemas, templates, and card examples discussed in 
the paper:

|Dir|Content|
|---|:---:|
|`lmdc/cards`|Generated examples for different card types in yaml and rdf format.|
|`lmdc/schemas`|Schema definition depicting how the card content is expected to be filled in.|
|`lmdc/templates`|Sample templates that can be re-used to generate cards.|
|`scripts`|Script to validate newly created cards against the expected schema.|