Name:     ocaml-flac

Version:  0.1.3
Release:  1
Summary:  OCaml bindings for flac
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-flac
Source0:  https://github.com/savonet/ocaml-flac/releases/download/%{version}/ocaml-flac-%{version}.tar.gz
Patch0:   ocaml-flac-0.1.3-bytes-compat.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ogg
BuildRequires: flac-devel
Requires:      flac

%prep
%setup -q 
%patch0

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

%description
OCAML bindings for flac


%changelog
* Sun Oct  8 2016 Lucas Bickel <hairmare@rabe.ch>
- Version bump

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-flac.spec
