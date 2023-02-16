# stock-price-notifier
Python Script that scheduled on GitHub Actions to run and notify through the messages everyday morning/afternoon about the Stock Price.

## Resources that helped me a lot

Articles that I read to get started
* [Article - #1](https://towardsdatascience.com/github-actions-everything-you-need-to-know-to-get-started-537f1dffa0ed)
* [Article - #2](https://towardsdatascience.com/introduction-to-github-actions-7fcb30d0f959)

To keep the user credentials secret
* [Creating encrypted secrets for a repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository)

A website to quickly check the scheduled time with a cron syntax is,
* [Crontab Guru](https://crontab.guru/)

GitHub Actions works based on `UTC` standard, But, I am from India, India follows `IST` standard time. So, I have to convert IST standard time to UTC standard time to trigger my python script on the exact IST standard time. I have used the following website to Change IST standard time to UTC standard time.
* [UTC to IST Converter](https://savvytime.com/converter/utc-to-ist)
