Summary:	Pack of themes for IceWM
Summary(pl):	Zestaw tematów dla IceWM
Name:		icewm-themes-pack4
Version:	1.0
Release:	3
License:	GPL (?)
Group:		Themes
Group(de):	Themen
Group(pl):	Motywy
Source0:	%{name}.tar.gz
Requires:	icewm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/X11R6/lib/X11/icewm/themes

%description
This is a set of 8 themes for IceWM.
blue metal				Sawsedge <sawsedge@yahoo.com>
BlueSteel				Bas Leerintveld
CubeX					<dwl@wolsi.com>
Fire95					<dwl@wolsi.com>
greenflat				slow
mcalamari				slow
Phaaba					Micha³ Szota <michal@k.pl>
YAK - Yet Another KDE 2.x clone		Sawsedge <sawsedge@yahoo.com>

%description -l pl
Jest to zestaw 8 tematów do uprzyjemnienia wygl±du twojego IceWMa.
blue metal				Sawsedge <sawsedge@yahoo.com>
BlueSteel				Bas Leerintveld
CubeX					<dwl@wolsi.com>
Fire95					<dwl@wolsi.com>
greenflat				slow
mcalamari				slow
Phaaba					Micha³ Szota <michal@k.pl>
YAK - Yet Another KDE 2.x clone		Sawsedge <sawsedge@yahoo.com>

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*
