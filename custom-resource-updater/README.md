<h3> Custom Resource Updater </h3>

A macro to ensure that CloudFormation Custom Resources are updated at every stack update

<h3> Basic Usage </h3>

Specify the Logical IDs of the Custom Resources that you wish to update at every stack update as a separate section under the title <code>ResourcesToUpdate</code>. If the <code>ResourcesToUpdate</code> section is not specified, then all Custom Resources are updated.

<h3> How it works </h3>

When the ChangeSet is created, the Lambda function is invoked, and it appends a property <code>DummyProperty</code> to the Custom Resource, with a unique random string. This ensures that the resource is updated.

<h3> Author </h3>

Roshan Arvind Sivakumar

Cloud Support Associate<br>
Amazon Web Services
