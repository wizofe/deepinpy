#!/usr/bin/env python

from deepinpy.forwards import MultiChannelMRI
from deepinpy.models import ResNet, ResNet5Block
from deepinpy.recons.recon import Recon


class ResNetRecon(Recon):
    def __init__(self, hparams):
        super(ResNetRecon, self).__init__(hparams)

        if self.hparams.network == 'ResNet5Block':
            self.network = ResNet5Block(
                num_filters=self.hparams.latent_channels,
                filter_size=7,
                batch_norm=self.hparams.batch_norm,
            )
        elif self.hparams.network == 'ResNet':
            self.network = ResNet(
                latent_channels=self.hparams.latent_channels,
                num_blocks=self.hparams.num_blocks,
                kernel_size=7,
                batch_norm=self.hparams.batch_norm,
            )

    def batch(self, data):

        maps = data['maps']
        masks = data['masks']
        inp = data['out']

        self.A = MultiChannelMRI(
            maps,
            masks,
            l2lam=0.0,
            img_shape=data['imgs'].shape,
            use_sigpy=self.hparams.use_sigpy,
            noncart=self.hparams.noncart,
        )
        self.x_adj = self.A.adjoint(inp)

    def forward(self, y):
        return self.network(self.x_adj)

    def get_metadata(self):
        return {}
