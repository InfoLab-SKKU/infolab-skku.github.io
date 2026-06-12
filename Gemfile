source "https://rubygems.org"

# jekyll
gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.7"

# NOTE: do not add the `wdm` gem for faster Windows file-watching —
# wdm 0.2.0 crashes the `jekyll serve` watcher under Ruby 4.0 (tested 2026-06).
# Polling (the default) is slower but stable.

# Ruby 4.0 standard library gems
gem "logger"
gem "csv"
gem "ostruct"
gem "base64"
gem "strscan"
gem "bigdecimal"

# gem "html-proofer", "~> 5.0"  # commented out - requires libcurl

# plugins
group :jekyll_plugins do
  gem "jekyll-spaceship"
  gem "jekyll-sitemap"
  gem "jekyll-redirect-from"
  gem "jekyll-feed"
  gem "jekyll-last-modified-at"
end
