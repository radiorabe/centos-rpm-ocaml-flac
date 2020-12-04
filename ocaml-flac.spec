%define debug_package %{nil}

Name:     ocaml-flac
Version:  0.1.7
Release:  0.1%{?dist}
Summary:  OCaml bindings for flac

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-flac
Source0:  https://github.com/savonet/ocaml-flac/releases/download/v%{version}/ocaml-flac-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ogg-devel
BuildRequires: flac-devel
Requires:      flac


%description
OCAML bindings for flac


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}


%build
./configure \
   --prefix=%{_prefix} \
   --disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so.owner
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Thu Dec 3 2020 Lucas Bickel <hairmare@rabe.ch> - 0.1.7-0.1
- Bump to 0.1.7

* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 0.1.5-0.0
- Bump to 0.1.5

* Thu Jan 24 2019 Lucas Bickel <hairmare@rabe.ch> - 0.1.4-0.1
- Bump to 0.1.4

* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.1.3-4
- Cleanup and add separate -devel subpackage

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.1.3-3
- Fix Fedora build by disabling debug package
