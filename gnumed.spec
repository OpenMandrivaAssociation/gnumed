Summary:	GNUmed client
Name:		gnumed
Version:	1.1.14
Release:	3
License:	GPLv2+
Group:		Office
Source0:		http://www.gnumed.de/downloads/client/%{version}/%{name}-client.%{version}.tgz
URL:		http://wiki.gnumed.de/

BuildArch:	noarch

BuildRequires:	pkgconfig(python2)
BuildRequires:	desktop-file-utils

%description
The GNUmed project builds free, liberated open source Electronic Medical Record
software in multiple languages to assist and improve longitudinal care
(specifically in ambulatory settings, i.e. multi-professional practices
and clinics).

It is developed by a handful of medical doctors and programmers from all
over the world.

It can be useful to anyone documenting the health of patients including,
but not limited to, doctors, physical therapists, occupational therapists,
acupuncturists, nurses, psychologists... 

%package client
Summary:	Client for %name
Group:		Office
Requires:	aspell
Requires:	file
Requires:	python-%{name}-client = %{version}
Requires:	%{name}-doc = %{version}
Requires:	python >= 2.3
Requires:	python-psycopg2 >= 2.0.10
Requires:	java
Requires:	xsane
Requires:	wxPythonGTK >= 2.6.3
Requires:	libreoffice-pyuno
Requires:	python-egenix-mx-base
Requires:	kdepim4
Requires:	texlive


%description client
The client for %name

%package -n python-%{name}-client
Summary:	Python libraries for %name client
Group:		Office
Requires:	python-%{name}-common = %{version}

%description -n python-%{name}-client
Common files for %name

%package -n python-%{name}-common
Summary:	Common files for %name
Group:		Office

%description -n python-%{name}-common
Common files for %name

%package doc
Summary:	Documentation for %name
Group:		Office

%description doc
Documentation for %name

%prep
%setup -qn %{name}-client.%{version}
%{__sed} -i -e 's@Exec=/usr/bin/gnumed@Exec=/usr/bin/gnumed --conf-file=/etc/%{name}/%{name}-client.conf@' client/%{name}-client.desktop

%build

%install

install -D -m 644 client/connectors/gm_ctl_client.conf %{buildroot}/etc/gnumed/gm_ctl_client.conf
install -D -m 644 client/doc/gnumed.conf.example %{buildroot}/etc/gnumed/gnumed.conf
install -D -m 644 client/etc/gnumed/gnumed-client.conf.example %{buildroot}/etc/gnumed/gnumed-client.conf
install -D -m 755 client/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 client/bitmaps/empty-face-in-bust.png %{buildroot}%{_datadir}/%{name}/bitmaps/empty-face-in-bust.png
install -D -m 644 client/bitmaps/gnumedlogo.png %{buildroot}%{_datadir}/%{name}/bitmaps/gnumedlogo.png
install -D -m 644 client/bitmaps/serpent.png %{buildroot}%{_datadir}/%{name}/bitmaps/serpent.png

for lang in de el es fr it nb nl pl pt pt_BR ru
do
install -D -m 644 client/po/${lang}-gnumed.mo %{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/gnumed.mo
done
%find_lang %{name}

#mkdir -p %{buildroot}%{_datadir}/pixmaps
#cp client/bitmaps/gnumed.xpm %{buildroot}%{_datadir}/pixmaps/gnumed.xpm

#install -d -m 755  %{buildroot}%{py_sitedir}/Gnumed/
#cp -r client/business client/exporters client/wxGladeWidgets client/wxpython client/gnumed.py %{buildroot}%{py_sitedir}/Gnumed
install -d -m 755 %{buildroot}%{py_sitedir}/Gnumed/business %{buildroot}%{py_sitedir}/Gnumed/exporters %{buildroot}%{py_sitedir}/Gnumed/wxGladeWidgets %{buildroot}%{py_sitedir}/Gnumed/wxpython/gui
install -m 644 client/__init__.py %{buildroot}%{py_sitedir}/Gnumed/
install -m 755 client/gnumed.py %{buildroot}%{py_sitedir}/Gnumed/
install -m 755 client/sitecustomize.py %{buildroot}%{py_sitedir}/Gnumed/
install -m 644 client/business/*.py %{buildroot}%{py_sitedir}/Gnumed/business
install -m 644 client/exporters/*.py %{buildroot}%{py_sitedir}/Gnumed/exporters
install -m 755 client/wxGladeWidgets/wxg*.py %{buildroot}%{py_sitedir}/Gnumed/wxGladeWidgets
install -m 644 client/wxGladeWidgets/__init__.py %{buildroot}%{py_sitedir}/Gnumed/wxGladeWidgets
install -m 644 client/wxpython/*.py %{buildroot}%{py_sitedir}/Gnumed/wxpython
install -m 644 client/wxpython/gui/*.py %{buildroot}%{py_sitedir}/Gnumed/wxpython/gui

install -D -m 644 client/bitmaps/%{name}logo.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 client/bitmaps/gm_icon-serpent_and_gnu.png %{buildroot}%{_iconsdir}/gm_icon-serpent_and_gnu.png

desktop-file-install \
	--vendor='' \
	--dir %{buildroot}%{_datadir}/applications \
	client/%{name}-client.desktop

# Files for common package
install -d -m 755 %{buildroot}%{py_sitedir}/Gnumed/pycommon
install -m 644 client/pycommon/*.py %{buildroot}%{py_sitedir}/Gnumed/pycommon
install -m 644 client/__init__.py %{buildroot}%{py_sitedir}/Gnumed

# Files for the doc package
install -d -m 755 %{buildroot}%{_defaultdocdir}/%{name}/user-manual
cp -r client/doc/user-manual/* %{buildroot}%{_defaultdocdir}/%{name}/user-manual
install -d -m 755 %{buildroot}%{_defaultdocdir}/%{name}/api
cp -r client/doc/api/* %{buildroot}%{_defaultdocdir}/%{name}/api

%files client -f %{name}.lang
%doc client/CHANGELOG
%config(noreplace)%{_sysconfdir}/%{name}/*
%{_bindir}/%name
%{_datadir}/%{name}
%{_datadir}/applications/gnumed-client.desktop
%{_iconsdir}/gnumed.png
%{_iconsdir}/gm_icon-serpent_and_gnu.png

%files -n python-%{name}-client
%doc client/CHANGELOG
%{py_sitedir}/Gnumed/business/
%{py_sitedir}/Gnumed/exporters/
%{py_sitedir}/Gnumed/wxGladeWidgets/
%{py_sitedir}/Gnumed/wxpython/

%files -n python-%{name}-common
%doc client/CHANGELOG
%{py_sitedir}/Gnumed/*.py
%{py_sitedir}/Gnumed/pycommon

%files doc
%doc client/CHANGELOG
%{_defaultdocdir}/%{name}/user-manual
%{_defaultdocdir}/%{name}/api


%changelog
* Mon May 21 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.14-1
+ Revision: 799756
- update to 1.1.14

* Thu Apr 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.13-1
+ Revision: 792129
- update to 1.1.13

* Sat Feb 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.12-1
+ Revision: 772844
- update to 1.1.12

* Sat Dec 17 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.7-1
+ Revision: 743195
- update to 1.1.7

* Fri Dec 02 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1.6-1
+ Revision: 737176
- imported package gnumed

