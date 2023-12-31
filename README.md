# AutoGPT_LINE
A webhook connector for the LINE using the Auto-GPT framework. This plugin allows you to easily integrate LINE with the powerful language model GPT-4 to create various automations and applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Plugin Installation Steps](#plugin-installation-steps)
- [Connect the .ENV](#connect-the-env)
- [Set up LINE](#set-up-LINE)
- [Processing the data](#processing-the-data)
- [Testing](#testing)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following:

- Auto-GPT repository
- An LINE account

## Plugin Installation Steps

1. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

2. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin:

   ```shell
   ALLOWLISTED_PLUGINS=example-plugin1,example-plugin2,example-plugin3
   ```

## Connect the .ENV

Add this to your .env to get AutoGPT to send to the right endpoint.

```
################################################################################
### AUTOGPT LINE Webhook Integration
################################################################################
ZAPIER_WEBHOOK_ENDPOINT=<your trigger is here>
```

## Set up LINE

LINE requires a webhooks connector.
1. Create a new Zap or modify an existing one
2. Add "Catch Hook in Webhooks by LINE" to the Zap. 
3. Set it up to Catch Hook.
Note that there's some trickiness to getting this to work well - you have to post data to it, but you haven't set anything up yet. the test that they provide will post some rudimentary data, but you'll have the ability to process any type of data - so you might have to revisit this page after AutoGPT is configured.
4. The webhook trigger will be shown to you in the UI. Put it in your ```ZAPIER_WEBHOOK_ENDPOINT``` env variable above.

Once added, you'll have to go to the documentation button to find your specific key. The key will route your json content to you will be posting.

## Processing the data

Once the first post works, you'll have a JSON value going into LINE. Use a JavaScript filter to make decisions about your content.


## Testing

To test the integration, perform the following steps:

1. Send a sample request to AutoGPT - for example, "Get the latest joke of the day and send it to me via LINE".
2. Verify that the request is received by LINE
3. Check the processing logic and ensure it is working as expected

## Usage

After successful testing, you can start using this plugin to create various automations and applications with the help of the GPT-4 language model and LINE.

## Troubleshooting

If you encounter any issues while using the plugin, refer to the following:

- Check the `.env` file for proper configuration.
- Verify that the LINE webhook trigger name and key are correct.
- Inspect the LINE applet configuration and ensure it is set up properly.
- Review the JavaScript filter for any syntax errors or logical issues.
- Check the Auto-GPT logs for any errors or warnings related to the plugin.

## Contributing

We welcome contributions to the AutoGPT_LINE plugin! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes, ensuring they adhere to the project's coding standards and guidelines.
4. Submit a pull request with a detailed description of your changes.

Please note that by contributing to this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).
