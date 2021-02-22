import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):

        if not name:
            name = 'Antifa'
        return 'Rosen auf den Weg gestreut : Ihr müsst sie lieb und nett behandeln, erschreckt sie nicht - sie sind so zart! Ihr müsst mit Palmen sie umwandeln, getreulich ihrer Eigenart! Pfeift euerm Hunde, wenn er kläfft - Küsst die Faschisten, wo ihr sie trefft! Wenn sie in ihren Sälen hetzen, sagt: Ja und Amen - aber gern! Hier habt ihr mich - schlagt mich in Fetzen! Und prügeln sie, so lobt den Herrn. Denn Prügeln ist doch ihr Geschäft! Küsst die Faschisten, wo ihr sie trefft. Und schießen sie - du lieber Himmel, schätzt ihr das Leben so hoch ein? Das ist ein Pazifisten-Fimmel! Wer möchte nicht gern Opfer sein? Nennt sie: Die süßen Schnuckerchen, gebt ihnen Bonbons und Zuckerchen... Und verspürt ihr auch in eurem Bauch den Hitler-Dolch, tief, bis zum Heft- Küsst die Faschisten, küsst die Faschisten, küsst die Faschisten, wo ihr sie trefft! - (Kurt Tucholsky)'

if __name__ == "__main__":
    app.run()