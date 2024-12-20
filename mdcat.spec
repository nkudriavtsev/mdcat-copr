Name: mdcat
Version: 2.7.1
Release: 1%{?dist}
Summary: cat for CommonMark
License: Mozilla Public License 2.0
URL: https://github.com/lunaryorn/mdcat/
Source0: https://github.com/lunaryorn/mdcat/archive/refs/tags/mdcat-%{version}.tar.gz
BuildRequires: cargo
BuildRequires: rubygem-asciidoctor
BuildRequires: openssl-devel
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
cargo build --release --no-default-features
asciidoctor -b manpage mdcat.1.adoc


%install
install -D -p -s -m 755 target/release/mdcat %{buildroot}%{_bindir}/mdcat
install -D -p -s -m 755 target/release/mdcat %{buildroot}%{_bindir}/mdcat
install -D -p -m 644 mdcat.1 %{buildroot}%{_mandir}/man1/mdcat.1


%check
cargo test --no-default-features


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/mdcat
%{_mandir}/man1/*

%changelog
%autochangelog
