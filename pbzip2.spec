%global debug_package %{nil}
Name:           pbzip2
Version:        1.1.13
Release:        1
Summary:        Parallel implementation of the bzip2 block-sorting file compressor
License:        BSD
URL:            http://www.compression.ca/pbzip2/

Source0:        https://launchpad.net/pbzip2/1.1/1.1.13/+download/pbzip2-1.1.13.tar.gz
Patch0:       001-Fix-Invalid-Suffix_pbzip2.patch

BuildRequires:  gcc-c++ bzip2-devel

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file compressor.  
The output of this version should be fully compatible with bzip2 v1.0.2 or newer 
(ie: anything compressed with pbzip2 can be decompressed with bzip2).

%package_help

%prep
%autosetup -n pbzip2-%{version} -p1
f=AUTHORS; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 && mv $f.utf8 $f && alias rpmbuild='rpmbuild --nodebuginfo' 

%build
%set_build_flags
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="%{__global_ldflags}"


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
* Fri Feb 03 2023 wenchaofan <349464272@qq.com> - 1.1.13-1
- Update to 1.1.13

* Fri Jan 10 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.1.12-10
- Package init
