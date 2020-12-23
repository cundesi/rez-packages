default_shell = "pwsh"
set_prompt = False

pip_install_remaps = [
    # Typical bin copy behaviour
    # Path in record          | pip installed to    | copy to rez destination
    # ------------------------|---------------------|--------------------------
    # ../../bin/*             | bin/*               | bin/*
    {
        "record_path": r"^{p}{s}{p}{s}(bin{s}.*)",
        "pip_install": r"\1",
        "rez_install": r"\1",
    },
    # Fix for https://github.com/nerdvegas/rez/issues/821
    # Path in record          | pip installed to    | copy to rez destination
    # ------------------------|---------------------|--------------------------
    # ../../lib/python/*      | *                   | python/*
    {
        "record_path": r"^{p}{s}{p}{s}lib{s}python{s}(.*)",
        "pip_install": r"\1",
        "rez_install": r"python{s}\1",
    },
    # Path in record          | pip installed to    | copy to rez destination
    # ------------------------|---------------------|--------------------------
    # ../../lib/python/*      | *                   | python/*
    {
        "record_path": r"^{p}{s}{p}{s}(.*)",
        "pip_install": r"\1",
        "rez_install": r"\1",
    },
    # Path in record          | pip installed to    | copy to rez destination
    # ------------------------|---------------------|--------------------------
    # ../site-packages/*      | *                   | python/*
    {
        "record_path": r"^{p}{s}site-packages{s}(.*)",
        "pip_install": r"\1",
        "rez_install": r"python{s}\1",
    },

]
