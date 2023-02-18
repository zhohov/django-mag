{ pkgs }: {
  deps = [
    pkgs.python38Full
    pkgs.chromium
    pkgs.chromedriver
  ];
  env = {
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}