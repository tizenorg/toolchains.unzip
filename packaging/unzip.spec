#specfile originally created for Fedora, modified for Moblin Linux
Summary: A utility for unpacking zip files
Name: unzip
Version: 6.0
Release: 9
License: BSD
Group: Applications/Archiving
Source: ftp://ftp.info-zip.org/pub/infozip/src/unzip60.tar.gz
# Not sent to upstream.
Patch1: unzip-6.0-bzip2-configure.patch
# Upstream plans to do this in zip (hopefully also in unzip).
Patch2: unzip-6.0-exec-shield.patch
# Upstream plans to do similar thing.
Patch3: unzip-6.0-close.patch
# Details in rhbz#532380.
# Reported to upstream: http://www.info-zip.org/board/board.pl?m-1259575993/
Patch4: unzip-6.0-attribs-overflow.patch
# Not sent to upstream, as it's Fedora/RHEL specific.
# Modify the configure script not to request the strip of binaries.
Patch5: unzip-6.0-nostrip.patch
URL: http://www.info-zip.org/pub/infozip/UnZip.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The unzip utility is used to list, test, or extract files from a zip
archive.  Zip archives are commonly found on MS-DOS systems.  The zip
utility, included in the zip package, creates zip archives.  Zip and
unzip are both compatible with archives created by PKWARE(R)'s PKZIP
for MS-DOS, but the programs' options and default behaviors do differ
in some respects.

Install the unzip package if you need to list, test or extract files from
a zip archive.

%prep
%setup -q -n %{name}60
%patch1 -p1 -b .bzip2-configure
%patch2 -p1 -b .exec-shield
%patch3 -p1 -b .close
%patch4 -p1 -b .attribs-overflow
%patch5 -p1 -b .nostrip
ln -s unix/Makefile Makefile

%build
make CFLAGS="-D_LARGEFILE64_SOURCE" linux_noasm LF2="" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 INSTALL="cp -p" install LF2="" 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README BUGS LICENSE 
%{_bindir}/*
%doc %{_mandir}/*/*

