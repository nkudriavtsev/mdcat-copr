Name: mdcat
Version: 0.26.1
Release: 1%{?dist}
Summary: cat for CommonMark
License: Mozilla Public License 2.0
URL: https://codeberg.org/flausch/mdcat.git
Source0: https://codeberg.org/flausch/mdcat/archive/mdcat-%{version}.tar.gz
BuildRequires: cargo
BuildRequires: rubygem-asciidoctor
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


%install
aux_dir=$(find . -path "./target/release/build/mdcat-*/out")
install -D -p -s -m 755 target/release/mdcat %{buildroot}%{_bindir}/mdcat
install -D -p -m 644 ${aux_dir}/mdcat.1 %{buildroot}%{_mandir}/man1/mdcat.1


%check
cargo test --no-default-features


%files
%license LICENSE
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md
%{_bindir}/mdcat
%{_mandir}/man1/*

%changelog
* Sun Apr 10 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.26.1-1
- Release 0.26.1
- Change repositiry hosting to https://codeberg.org/flausch/mdcat.git

* Mon Jul 05 2021 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.23.0-1
- Release 0.23.0

* Tue Feb 23 2021 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.22.3-1
- Release 0.22.3

* Tue Jan 12 2021 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.22.2-1
- Release 0.22.2
- License change

* Wed Oct 03 2018 Sebastian Wiesner <sebastian@swsnr.de> - 0.10.1-1
- Initial spec file
