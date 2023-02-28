Name: mdcat
Version: 1.1.0
Release: 1%{?dist}
Summary: cat for CommonMark
License: Mozilla Public License 2.0
URL: https://github.com/lunaryorn/mdcat/
Source0: https://github.com/lunaryorn/mdcat/archive/refs/tags/mdcat-%{version}.tar.gz
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
%doc README.md CHANGELOG.md
%{_bindir}/mdcat
%{_mandir}/man1/*

%changelog
* Tue Feb 28 2023 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 1.1.0-1
- Release 1.1.0

* Fri Dec 02 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.30.3-1
- Release 0.30.3

* Fri Dec 02 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.30.2-1
- Release 0.30.2

* Wed Nov 30 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.30.1-1
- Release 0.30.1

* Thu Oct 27 2022 Nicholas Kudriavtsev <nkudriavtsev@gmail.com> - 0.29.0-1
- Release 0.29.0
- Change repositiry hosting to https://github.com/lunaryorn/mdcat/

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
