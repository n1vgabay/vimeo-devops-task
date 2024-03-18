# Vimeo DevOps Task

[![Release Version](https://img.shields.io/github/v/release/username/repo.svg)](https://github.com/username/repo/releases/latest)
[![Build Status](https://img.shields.io/travis/username/repo/master.svg)](https://travis-ci.org/username/repo)
[![Coverage Status](https://img.shields.io/coveralls/github/username/repo/master.svg)](https://coveralls.io/github/username/repo)

This Flask application serves as a simple exchange rate converter. Users can input source currency, target currency, and the amount they wish to convert. The application fetches the latest exchange rates from an external API and calculates the converted amount based on the provided inputs. It provides a user-friendly interface for quick and convenient currency conversion.

[![Vimeo Diagram](https://i.ibb.co/yskPGkX/vimeo-diagram.png)](https://ibb.co/f0NFBN2)

CI/CD:
- Auto-deploy for dev env by commiting changes in GitOps repository (Example: override image tag in envs/dev/microservice/values.yaml)
- Manual workflow for microservices promotion between envs -> Open PR for apply new versions changes
- Release is created each time workflow is success run.
- First promotion needs to be for QA, which can have another invoke of workflow for automated testings.
- After microservices new version is tested on QA env, open PR can be created or be automated as well to be open when tests finished in order to upgrade stage env as well.
- Double approve for the recent changes in stage to verify functionalliy indeed applied without any issues.
- Then after release approved we can upgrade our prod envs for the relevant services taken into account for the upcoming company changes. The app is flexiable to take any config for the relevant enviornment.

* The value CURRENCYFREAKS_API_KEY in dev_config.json is for demo purposes only. Sensitive information shouldn't be in github and more likely to be pulled using some secure authentication.