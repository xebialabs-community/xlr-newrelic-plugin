# xlr-newrelic-plugin

This plugin provides a deployment notification task to NewRelic
It's based on the [Recording deployments](https://docs.newrelic.com/docs/apm/new-relic-apm/maintenance/recording-deployments) REST API

[![Build Status][xlr-newrelic-travis-image] ][xlr-newrelic-travis-url]
[![Build Status][xlr-newrelic-codacy-image] ][xlr-newrelic-codacy-url]
[![Build Status][xlr-newrelic-code-climate-image] ][xlr-newrelic-code-climate-url]


[xlr-newrelic-travis-image]: https://travis-ci.org/xebialabs-community/xlr-newrelic-plugin.svg?branch=master
[xlr-newrelic-travis-url]: https://travis-ci.org/xebialabs-community/xlr-newrelic-plugin
[xlr-newrelic-codacy-image]: https://api.codacy.com/project/badge/Grade/7e66235d52e3447c890c7c2e0ea9edb4
[xlr-newrelic-codacy-url]: https://www.codacy.com/app/rvanstone/xlr-newrelic-plugin
[xlr-newrelic-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xlr-newrelic-plugin/badges/gpa.svg
[xlr-newrelic-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xlr-newrelic-plugin


## New Relic setup

Before to use Newrelic deployment notification task, it's needed to setup a Newrelic server definition within the following information:

- **Title:** Name of the Newrelic server definition.
- **URL:** Base URL of the Newrelic server instance
- **ApiKey:** Generated API Key in Newrelic to allow REST access
- **Proxy URL:** Proxy URL to use in format `http://username:password@proxyurl:proxyport`, leave it in blank if isn't required.

## Deployment Notification task

The Deployment notification task needs the next information:

- **Revision:** A unique ID for this deployment usually a commit id or version
- **Changelog:** A summary of what changed in this deployment
- **Description:**  A high-level description of this deployment
- **User:** Identity of user/owner requesting deployment
- **ApplicationId:** Newrelic ID of the changed application
