AWS announced a new <a href = "https://aws.amazon.com/about-aws/whats-new/2018/09/introducing-aws-cloudformation-macros/">feature</a> in September 2018, Macros in CloudFormation, allowing customers to add custom logic to templates and modify the template as necessary. CloudFormation transforms help simplify template authoring by condensing the expression of AWS infrastructure as code and enabling reuse of template components.

<h4> How Macros Work : </h4>

There are two steps in the process of modifying templates using macros: A) Creating the Macro, and B) Using the Macro to  proces your templates. 

You can read more about how they work in the referenced AWS docs <a href = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">[1]</a>.

This repo is a small collection of Macros I've developed to add useful features to CloudFormation templates, for example, fetching Key-Value pairs from a DynamoDB and adding them to Mappings.

Feel free to go through them, and improve upon them as well!
