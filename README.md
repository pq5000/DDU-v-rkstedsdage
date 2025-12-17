# Vigtig information
Dette er **ikke vores endelige produkt**. Dette er bare hvor meget vi nåede at lave. Dette er grundet sygdom hos medlemmerne, og at vi ikke kunne få tilladelse til at 3D printe om mandagen. Dette resulterede i, at vi ikke på ingen måde kunne færdiggøre vores hydroponics-system

# Demo video af produkt
Der kan findes en demo video af hvor langt vi kom med den teknologiske side af produktet med **dette link**: https://youtu.be/5KJ7LcODG-Q

# Lidt om koden i dette repository
- watercycle.ino er koden på selve arduinoen. Den modtager et serial input fra computeren, som arduinoen er tilsluttet til.
- watercycle_reciever.py er koden der køre på den tilsuttede arduino. Den modtager signalet fra telefonen appen.
- watercycle_app.swift er koden for telefon appen. Det noteres, at denne kode var skabt med hjælp fra AI.

# Sådan den trådløse forbindelse virker og hvorfor vi ikke brugte Nano ESP32
Vi brugte ikke Nano ESP32 til vores trådløse forbindelse, da dens pins ikke var kraftfulde nok til at forbindes til 5V relays som er forbundet til 9V batterier. Derfor virker den trådløse forbindelse ved at forbinde Arduino Uno'en til at modtage et serial input fra computeren. Dette sendes fra appen til computeren via discord bots og discord webhooks. Dette er fordi vores produkt kun er en **alpha prototype** så vi mente at hoste en server med authentication etc. var unødvendigt.
