Summary:	Pack of themes for IceWM
Summary(pl):	Zestaw motywów dla IceWM-a
Name:		icewm-themes4
Version:	1.0
Release:	2
License:	GPL (?)
Group:		Themes
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	97725f034717ec01b6fd0180a187b45d
Requires:	icewm
Obsoletes:	icewm-themes-pack4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	/usr/share/icewm/themes

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
Jest to zestaw 8 motywów do uprzyjemnienia wygl±du twojego IceWM-a.
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
