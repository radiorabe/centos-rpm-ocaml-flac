%define debug_package %{nil}

Name:     ocaml-flac

Version:  0.1.3
Release:  3%{?dist}
Summary:  OCaml bindings for flac
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-flac
Source0:  https://github.com/savonet/ocaml-flac/releases/download/%{version}/ocaml-flac-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ogg
BuildRequires: flac-devel

Requires:      flac

%description
OCAML bindings for flac

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/flac/META
/usr/lib64/ocaml/flac/flac.a
/usr/lib64/ocaml/flac/flac.cma
/usr/lib64/ocaml/flac/flac.cmi
/usr/lib64/ocaml/flac/flac.cmxa
/usr/lib64/ocaml/flac/flac.mli
/usr/lib64/ocaml/flac/flac.cmx
/usr/lib64/ocaml/flac/ogg_demuxer_flac_decoder.cmi
/usr/lib64/ocaml/flac/ogg_demuxer_flac_decoder.cmx
/usr/lib64/ocaml/flac/ogg_demuxer_flac_decoder.mli
/usr/lib64/ocaml/flac/ogg_flac.cmi
/usr/lib64/ocaml/flac/ogg_flac.cmx
/usr/lib64/ocaml/flac/ogg_flac.mli
/usr/lib64/ocaml/flac/libflac_stubs.a
/usr/lib64/ocaml/stublibs/dllflac_stubs.so
/usr/lib64/ocaml/stublibs/dllflac_stubs.so.owner

%changelog
* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.1.3-3
- Fix Fedora build by disabling debug package
