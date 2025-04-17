This is how I installed and set up my neovim config
- Install via APT
```
sudo apt update                                                                                   # Refresh package lists :contentReference[oaicite:0]{index=0}
sudo apt install -y \
  shellcheck           \   # Bash scripts static analysis :contentReference[oaicite:1]{index=1}
  clang-tidy           \   # C/C++ static analysis :contentReference[oaicite:2]{index=2}
  hadolint             \   # Dockerfile linter (via prebuilt binary) :contentReference[oaicite:3]{index=3}
  gitlint              \   # Git commit/config linter
  commitlint           \   # Conventional commit linter
  gitignore-lint       \   # .gitignore syntax checks
  htmlhint             \   # HTML linter :contentReference[oaicite:4]{index=4}
  jq                   \   # JSON processor (syntax ≈ linter)
  jsonlint             \   # JSON syntax checker
  luacheck             \   # Lua diagnostics
  markdownlint         \   # Markdown linter
  nginx-lint           \   # Nginx config linter
  pemlint              \   # PEM file validation
  perlcritic           \   # Perl best practices
  phpcs                \   # PHP CodeSniffer
  phpmd                \   # PHP Mess Detector
  python3-pylint       \   # Python static checking :contentReference[oaicite:5]{index=5}
  python3-ruff         \   # (optional) fast Python linter
  rubocop              \   # Ruby linter
  sqlfluff             \   # SQL linter :contentReference[oaicite:6]{index=6}
  ssh-lint             \   # SSH config checks
  taplo                \   # TOML syntax and style (Taplo)
  csvkit               \   # CSV validation (via csvlint)
  vim-vint             \   # Vimscript linting
  xmlstarlet           \   # XML syntax tools (includes `xmllint`)
  yamllint             \   # YAML linter

```
- Install via NPM
```
sudo npm install -g \
  eslint_d              \   # Fast ESLint daemon :contentReference[oaicite:7]{index=7}
  eslint-plugin-jsdoc   \   # JSDoc rules for ESLint
  commentlint           \   # Comment style linter
  @commitlint/cli       \   # Conventional commits linter
  @commitlint/config-conventional \
  gitignore-lint        \
  htmlhint              \   # HTML linter :contentReference[oaicite:8]{index=8}
  javadoc-lint          \   # Javadoc syntax checker
```
- install via python3-* APT
```
sudo pip3 install --upgrade \
  pylint                \   # Python static analysis
  pip-check-reqs        \   # Find missing/extra requirements :contentReference[oaicite:9]{index=9}
  sqlfluff              \   # SQL linter :contentReference[oaicite:10]{index=10}
  httpie                \   # HTTP request syntax check
  markdownlint-cli      \   # Vale or markdownlint if desired
```
- GO based
```
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh \
  | sh -s -- -b "$(go env GOPATH)/bin"                                             # golangci-lint :contentReference[oaicite:11]{index=11}
```
- RUST based
```
rustup component add clippy                                                          # cargo clippy via Rustup :contentReference[oaicite:12]{index=12}
```
- .NET based
```
dotnet tool install -g csharpier                                                    # C# code style fixer
```
### Verify
```
shellcheck --version
clang-tidy --version
hadolint --version
eslint_d --version
python3 -m pylint --version
sqlfluff --version
golangci-lint --version
cargo clippy --version
```