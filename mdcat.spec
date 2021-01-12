Name: mdcat
Version: 0.22.2
Release: 1%{?dist}
Summary: cat for CommonMark
License: Mozilla Public License 2.0
URL: https://github.com/lunaryorn/mdcat/
Source0: https://github.com/lunaryorn/mdcat/archive/mdcat-%{version}/mdcat-%{version}.tar.gz
BuildRequires: cargo
%if 0%{?fedora} >= 24
ExclusiveArch: x86_64 i686 armv7hl
%else
ExclusiveArch: x86_64 aarch64
%endif


%description
mdcat renders CommonMark Markdown documents to TTYs, with support for links and
images.

# Disable debug info; mdcat doesn't include debug info in release profile
%define debug_package %{nil}
%prep
%autosetup -v -n mdcat-mdcat-%{version}


%build
# Build only relevant terminals for Linux
cargo build --release --no-default-features --features terminology


%install
install -D -p -m 755 target/release/mdcat %{buildroot}%{_bindir}/mdcat


%check
cargo test --no-default-features --features terminology


%files
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_bindir}/mdcat

%changelog
* Tue 12 2021 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.22.2-1
- Release 0.22.2
- License change

* Wed Oct 03 2018 Sebastian Wiesner <sebastian@swsnr.de> - 0.10.1-1
- Initial spec file
