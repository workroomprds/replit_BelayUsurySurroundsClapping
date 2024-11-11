{pkgs}: {
  deps = [
    pkgs.nano
    pkgs.haskellPackages.ShellCheck
    pkgs.jq
    pkgs.vim
    pkgs.q
  ];
}
