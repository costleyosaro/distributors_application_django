from dashboard.models import Product

image_url_map = {
    "kvlwpxpyued03fz960rk.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751955340/kvlwpxpyued03fz960rk.jpg",
    "jwwgvvy4fdplcrm4unrc.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904538/jwwgvvy4fdplcrm4unrc.png",
    "d9ttk36bhimzeoldstyk.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904528/d9ttk36bhimzeoldstyk.png",
    "dhougsbmn72x4fp9rwxk.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904505/dhougsbmn72x4fp9rwxk.png",
    "kqockazxnfvq9avtexnk.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904495/kqockazxnfvq9avtexnk.png",
    "omvbbbmtaqwbh6dejapd.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904484/omvbbbmtaqwbh6dejapd.png",
    "fccjwj0mrscc7586knjt.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904476/fccjwj0mrscc7586knjt.png",
    "axv5zxs8hvkbol9nrqmg.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904468/axv5zxs8hvkbol9nrqmg.png",
    "unsjl8payqyrt6aznqqv.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904457/unsjl8payqyrt6aznqqv.png",
    "hpff7ajeqwtvqu7cijn0.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904450/hpff7ajeqwtvqu7cijn0.png",
    "ppbol3catubhgwhpgibn.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904444/ppbol3catubhgwhpgibn.png",
    "sojvrejoyr8t593qaoz5.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904436/sojvrejoyr8t593qaoz5.png",
    "zulcbgowdmeoilwbwgrt.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904423/zulcbgowdmeoilwbwgrt.png",
    "r8blm3kjleuryzfzxsjc.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904415/r8blm3kjleuryzfzxsjc.png",
    "rgt0vsazx4mzxn7fr2ey.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904404/rgt0vsazx4mzxn7fr2ey.jpg",
    "fg3qieev91jrucao2cz6.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904400/fg3qieev91jrucao2cz6.jpg",
    "mes9hinzmvabhadferwk.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904398/mes9hinzmvabhadferwk.jpg",
    "rggsj65uxonl1ulba9an.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904396/rggsj65uxonl1ulba9an.jpg",
    "qtfonxcarzv48jrqoqnw.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904389/qtfonxcarzv48jrqoqnw.jpg",
    "v6mdmw4loobokqmn2td6.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904386/v6mdmw4loobokqmn2td6.jpg",
    "urnzmnsdmq8jgtv5xooy.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904380/urnzmnsdmq8jgtv5xooy.jpg",
    "mdmtygf17zuhiqjcwkc4.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904378/mdmtygf17zuhiqjcwkc4.jpg",
    "ubfykab5v9rfh2b1ehim.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904377/ubfykab5v9rfh2b1ehim.jpg",
    "c8ifjpy1w8mpt0hvhjiu.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904376/c8ifjpy1w8mpt0hvhjiu.jpg",
    "eaxh8cuue1cn5xjddlrc.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904373/eaxh8cuue1cn5xjddlrc.jpg",
    "ydfvbqxx63aaonakbgtz.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904371/ydfvbqxx63aaonakbgtz.jpg",
    "ypgaxwbzhzs3f7zukjxh.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904369/ypgaxwbzhzs3f7zukjxh.jpg",
    "bseqz2xeerqgkvlcdrmg.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904366/bseqz2xeerqgkvlcdrmg.jpg",
    "jq55ggbqhtyg5r0cv3nl.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904365/jq55ggbqhtyg5r0cv3nl.jpg",
    "qkd8mnhi649pjnfloqwt.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904361/qkd8mnhi649pjnfloqwt.jpg",
    "wtpceteidhbueq9g6b5k.webp": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904360/wtpceteidhbueq9g6b5k.webp",
    "vo420bzdmyeo44j9abnw.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904357/vo420bzdmyeo44j9abnw.jpg",
    "luwgpyr7eau6z2phfzt5.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904355/luwgpyr7eau6z2phfzt5.jpg",
    "ywd9troytfdnnifc9w7l.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904353/ywd9troytfdnnifc9w7l.jpg",
    "rpafwvcpwfsnabhbr78f.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904352/rpafwvcpwfsnabhbr78f.jpg",
    "ytys0rojclna7welbs03.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904350/ytys0rojclna7welbs03.jpg",
    "gfm5d0myblryqkraz2h4.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904348/gfm5d0myblryqkraz2h4.webp",
    "bljov2flwd9sg1fyyrwx.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904343/bljov2flwd9sg1fyyrwx.webp",
    "ucvq9qlxofhbcvjha4kg.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904335/ucvq9qlxofhbcvjha4kg.webp",
    "is6rbwxulk592ogw7tqg.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904333/is6rbwxulk592ogw7tqg.webp",
    "rbo5mhqicgzw22nwormh.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904330/rbo5mhqicgzw22nwormh.jpg",
    "gzcupixocpboscloykrr.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904328/gzcupixocpboscloykrr.webp",
    "ghmshqu7upk2nx6iiipo.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904323/ghmshqu7upk2nx6iiipo.webp",
    "gygkycepjhmgl6vh3zxc.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904319/gygkycepjhmgl6vh3zxc.jpg",
    "jjzn5vvujtfr8vx56puf.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904317/jjzn5vvujtfr8vx56puf.jpg",
    "ghiwy3cmyswqbws4ein4.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904314/ghiwy3cmyswqbws4ein4.jpg",
    "ejdrhnwcf3byvjhcmejw.webp" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904308/ejdrhnwcf3byvjhcmejw.webp",
    "rwyws7nvpttdmqjle481.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904299/rwyws7nvpttdmqjle481.jpg",
    "wtcpfsh42uk0vsqn9i6x.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904293/wtcpfsh42uk0vsqn9i6x.jpg",
    "xmikuewmbx4zokrvohtg.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904290/xmikuewmbx4zokrvohtg.jpg",
    "pnq1h0npyzpygspskmsm.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904284/pnq1h0npyzpygspskmsm.jpg",
    "bjg1ricspt66guf2z7yl.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904282/bjg1ricspt66guf2z7yl.jpg",
    "vbffzespcytsxadmfv72.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904279/vbffzespcytsxadmfv72.jpg",
    "ipzh8asgrmwzrnlxjuev.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904274/ipzh8asgrmwzrnlxjuev.jpg",
    "ewjurnzw3vw1yf9qoc21.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904272/ewjurnzw3vw1yf9qoc21.jpg",
    "tmfntqbuvqkahvxwskhq.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904269/tmfntqbuvqkahvxwskhq.jpg",
    "o5herkfbulctwgalsflz.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904264/o5herkfbulctwgalsflz.jpg",
    "hwcrq6vtthqe9iepabmr.jpg" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904262/hwcrq6vtthqe9iepabmr.jpg",
    "awnycs4v96udtal1mg1j.png" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904260/awnycs4v96udtal1mg1j.png",
    "eslxcivbx4ym6hrxp1yo.png" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904248/eslxcivbx4ym6hrxp1yo.png",
    "motrrlral8qvuagmj5gt.png" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904242/motrrlral8qvuagmj5gt.png",
    "bb2mfbxq6qwvyza6bzyf.png" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904234/bb2mfbxq6qwvyza6bzyf.png",
    "prklc9esxgddxq0foisw.png" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904229/prklc9esxgddxq0foisw.png",
    "sfecqeds2gmlfjtbekeh.png" : "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904223/sfecqeds2gmlfjtbekeh.png",
    "h635lc3qdnlgbfoskwsj.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904214/h635lc3qdnlgbfoskwsj.png",
    "o8ahphvcilouskfqnhv1.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904205/o8ahphvcilouskfqnhv1.png",
    "qfbhtc65nopxc3iil5ca.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904202/qfbhtc65nopxc3iil5ca.png",
    "sy0cb1o1iikhdd7hurie.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904196/sy0cb1o1iikhdd7hurie.png",
    "uwgzauhbp1nvpb6yny5a.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904186/uwgzauhbp1nvpb6yny5a.png",
    "lb40z1gvbln5n32kgazz.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904183/lb40z1gvbln5n32kgazz.png",
    "l4mwq4ominwawxrhzyk5.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904181/l4mwq4ominwawxrhzyk5.png",
    "wweo8uhhb9l6bisq8irv.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904180/wweo8uhhb9l6bisq8irv.jpg",
    "ixb0dofgqh1juyg7st60.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904179/ixb0dofgqh1juyg7st60.jpg",
    "ai7ifw4krw2dctkn73ho.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904177/ai7ifw4krw2dctkn73ho.jpg",
    "irjzzphnaxxscwtw7tkm.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904172/irjzzphnaxxscwtw7tkm.jpg",
    "hvbyjvbulevmu1yot0ji.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904170/hvbyjvbulevmu1yot0ji.jpg",
    "v6xtvrotrjanfcbenr0o.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904167/v6xtvrotrjanfcbenr0o.png",
    "rgtra7vfqb3fhunr4wup.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904163/rgtra7vfqb3fhunr4wup.png",
    "pxeaaffxqnhdrfjecdnn.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904160/pxeaaffxqnhdrfjecdnn.jpg",
    "oujlk7txoap3qd78yppn.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904157/oujlk7txoap3qd78yppn.png",
    "cpcvh2gbhrnqknuqf2ld.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904153/cpcvh2gbhrnqknuqf2ld.png",
    "z1a6nmi4ky1l7rafymvx.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904148/z1a6nmi4ky1l7rafymvx.jpg",
    "v7blhxasppcyfn4anqne.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904144/v7blhxasppcyfn4anqne.jpg",
    "kt6jbhhmgkibb9nu8st0.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904142/kt6jbhhmgkibb9nu8st0.png",
    "esz4vjf8r8utdqt1xznk.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904139/esz4vjf8r8utdqt1xznk.jpg",
    "fttvdmfr4ie5qmfylonf.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904136/fttvdmfr4ie5qmfylonf.png",
    "llil73o4tuss0bxdgxes.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904129/llil73o4tuss0bxdgxes.png",
    "ss1ov4cksukxexgitqwu.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751904123/ss1ov4cksukxexgitqwu.png",
    "kmnqehvu5ymedzkoqhdp.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751892070/kmnqehvu5ymedzkoqhdp.jpg",
    "cld-sample-5.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751403463/cld-sample-5.jpg",
    "cld-sample-3.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751403463/cld-sample-3.jpg",
    "cld-sample-4.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751403463/cld-sample-4.jpg",
    "cld-sample-2.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751403463/cld-sample-2.jpg",
    "cld-sample.jpg": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751403463/cld-sample.jpg",
    "logo.png": "https://res.cloudinary.com/djq2ywwry/image/upload/v1751403462/samples/logo.png",
    }
 


updated = 0
skipped = 0

for product in Product.objects.all():

    filename = product.image.name.split("/")[-1]
    if filename in image_url_map:
        product.image = image_url_map[filename]
        product.save()
        updated += 1
        print(f"✅ Updated {product.name} with image: {image_url_map[filename]}")
    else:
        skipped += 1
        print(f"❌ Skipped {product.name} — image not found for: {filename}")

print(f"\n🎉 Done! Updated: {updated}, Skipped: {skipped}")