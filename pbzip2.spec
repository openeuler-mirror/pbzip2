Name:           pbzip2
Version:        1.1.12
Release:        11
Summary:        Parallel implementation of the bzip2 block-sorting file compressor
License:        BSD
URL:            http://www.compression.ca/pbzip2/

Source0:        http://launchpad.net/pbzip2/1.1/1.1.12/+download/pbzip2-%{version}.tar.gz
Patch0:         pbzip2-1.1.12-buildflags.patch

BuildRequires:  gcc-c++ bzip2-devel

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file compressor.  
The output of this version should be fully compatible with bzip2 v1.0.2 or newer 
(ie: anything compressed with pbzip2 can be decompressed with bzip2).

%package_help

%prep
%autosetup -n pbzip2-%{version} -p1
f=AUTHORS; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 && mv $f.utf8 $f

%build
%set_build_flags
%make_build


%install
pushd %{buildroot}
install -D -m755 %{_builddir}/pbzip2-%{version}/pbzip2 .%{_bindir}/pbzip2
install -D -m644 %{_builddir}/pbzip2-%{version}/pbzip2.1 .%{_mandir}/man1/pbzip2.1
ln -sf %{_builddir}/pbzip2-%{version}/pbzip2 .%{_bindir}/pbunzip2
ln -sf %{_builddir}/pbzip2-%{version}/pbzip2 .%{_bindir}/pbzcat
popd

%files
%defattr(-,root,root)
%doc AUTHORS README
%license COPYING
%{_bindir}/*

%files help
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/man1/*

%changelog
* Thu Nov 10 2022 liyanan <liyanan32@h-partners.com>  - 1.1.12-11
- Change source

* Fri Jan 10 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.1.12-10
- Package init
