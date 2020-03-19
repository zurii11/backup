'use strict';

class main extends Phaser.Scene {
    constructor() {
        super({key:"main"});
    }

    preload() {
        this.load.image('a', 'assets/MONONOKE.jpg');
    }

    create() {
        this.image = this.add.image(100, 100, 'a');
    }
}