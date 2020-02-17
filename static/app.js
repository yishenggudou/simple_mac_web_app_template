(function () {
    class TimgerApp {
        static getInstance(name) {
            if (!this.instance) {
                this.instance = new TimgerApp(name);
            }
            return this.instance;
        }

        constructor(name) {
            this.name = name;
            this.instance = null;
        }

        setupAd() {

        }

        setupTrace() {

        }

        setupLink() {
            setInterval(function () {
                $(document).find('[target=_blank]').attr('target', 'none')
            }, 1000)
        }
    }

    window.onload = function () {
        if (window.jQuery) {

            console.log("jquery has installed!");
        } else {
            // jQuery is not loaded
            console.log("jquery has installed!");

        }
    };
})()